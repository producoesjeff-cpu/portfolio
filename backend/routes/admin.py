from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import List, Optional
import logging
from datetime import datetime

from models.admin import AdminUser, AdminLogin, AdminResponse, AdminCreate
from models.portfolio import Portfolio, PortfolioUpdate
from models.project import Project, ProjectCreate, ProjectUpdate
from models.client import Client, ClientCreate, ClientUpdate
from models.message import ContactMessage, ContactMessageUpdate
from services.auth import (
    hash_password, verify_password, create_access_token, 
    verify_token, create_admin_response
)
from utils.database import (
    get_admin_collection, get_portfolio_collection,
    get_projects_collection, get_clients_collection,
    get_messages_collection
)
from utils.config import get_config

logger = logging.getLogger(__name__)
router = APIRouter()
security = HTTPBearer()


# Dependência para verificar autenticação
async def get_current_admin(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Verifica se o usuário está autenticado"""
    try:
        token = credentials.credentials
        payload = verify_token(token)
        username = payload.get("sub")
        
        admin_col = await get_admin_collection()
        admin = await admin_col.find_one({"username": username})
        
        if not admin:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuário não encontrado"
            )
        
        return AdminUser(**admin)
        
    except Exception as e:
        logger.error(f"Erro na autenticação: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido"
        )


@router.post("/login")
async def admin_login(login_data: AdminLogin):
    """Login do administrador"""
    try:
        admin_col = await get_admin_collection()
        admin = await admin_col.find_one({"username": login_data.username})
        
        if not admin or not verify_password(login_data.password, admin["passwordHash"]):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciais inválidas"
            )
        
        # Atualizar último login
        await admin_col.update_one(
            {"_id": admin["_id"]},
            {"$set": {"lastLogin": datetime.utcnow()}}
        )
        
        # Criar token
        access_token = create_access_token(data={"sub": admin["username"]})
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": create_admin_response(AdminUser(**admin))
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro no login: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Erro interno do servidor"
        )


@router.get("/portfolio")
async def get_admin_portfolio(current_admin: AdminUser = Depends(get_current_admin)):
    """Busca dados do portfólio para edição"""
    try:
        portfolio_col = await get_portfolio_collection()
        portfolio = await portfolio_col.find_one()
        
        if not portfolio:
            raise HTTPException(
                status_code=404,
                detail="Portfólio não encontrado"
            )
        
        return portfolio
        
    except Exception as e:
        logger.error(f"Erro ao buscar portfólio admin: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno")


@router.put("/portfolio")
async def update_portfolio(
    portfolio_update: PortfolioUpdate,
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Atualiza dados do portfólio"""
    try:
        portfolio_col = await get_portfolio_collection()
        
        update_data = {k: v for k, v in portfolio_update.dict().items() if v is not None}
        update_data["updatedAt"] = datetime.utcnow()
        
        result = await portfolio_col.update_one(
            {},
            {"$set": update_data},
            upsert=True
        )
        
        if result.modified_count == 0 and result.upserted_id is None:
            raise HTTPException(
                status_code=400,
                detail="Erro ao atualizar portfólio"
            )
        
        return {"success": True, "message": "Portfólio atualizado com sucesso"}
        
    except Exception as e:
        logger.error(f"Erro ao atualizar portfólio: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno")


@router.get("/projects")
async def get_admin_projects(current_admin: AdminUser = Depends(get_current_admin)):
    """Lista todos os projetos para admin"""
    try:
        projects_col = await get_projects_collection()
        projects = await projects_col.find().sort("createdAt", -1).to_list(100)
        
        return [Project(**project) for project in projects]
        
    except Exception as e:
        logger.error(f"Erro ao buscar projetos admin: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno")


@router.post("/projects")
async def create_project(
    project: ProjectCreate,
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Cria novo projeto"""
    try:
        projects_col = await get_projects_collection()
        
        new_project = Project(**project.dict())
        result = await projects_col.insert_one(new_project.dict())
        
        if not result.inserted_id:
            raise HTTPException(
                status_code=400,
                detail="Erro ao criar projeto"
            )
        
        return {"success": True, "message": "Projeto criado com sucesso", "id": new_project.id}
        
    except Exception as e:
        logger.error(f"Erro ao criar projeto: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno")


@router.put("/projects/{project_id}")
async def update_project(
    project_id: str,
    project_update: ProjectUpdate,
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Atualiza projeto existente"""
    try:
        projects_col = await get_projects_collection()
        
        update_data = {k: v for k, v in project_update.dict().items() if v is not None}
        update_data["updatedAt"] = datetime.utcnow()
        
        result = await projects_col.update_one(
            {"id": project_id},
            {"$set": update_data}
        )
        
        if result.modified_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Projeto não encontrado"
            )
        
        return {"success": True, "message": "Projeto atualizado com sucesso"}
        
    except Exception as e:
        logger.error(f"Erro ao atualizar projeto: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno")


@router.delete("/projects/{project_id}")
async def delete_project(
    project_id: str,
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Remove projeto"""
    try:
        projects_col = await get_projects_collection()
        
        result = await projects_col.delete_one({"id": project_id})
        
        if result.deleted_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Projeto não encontrado"
            )
        
        return {"success": True, "message": "Projeto removido com sucesso"}
        
    except Exception as e:
        logger.error(f"Erro ao remover projeto: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno")


@router.get("/clients")
async def get_admin_clients(current_admin: AdminUser = Depends(get_current_admin)):
    """Lista todos os clientes para admin"""
    try:
        clients_col = await get_clients_collection()
        clients = await clients_col.find().sort("order", 1).to_list(100)
        
        return [Client(**client) for client in clients]
        
    except Exception as e:
        logger.error(f"Erro ao buscar clientes admin: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno")


@router.post("/clients")
async def create_client(
    client: ClientCreate,
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Cria novo cliente"""
    try:
        clients_col = await get_clients_collection()
        
        new_client = Client(**client.dict())
        result = await clients_col.insert_one(new_client.dict())
        
        if not result.inserted_id:
            raise HTTPException(
                status_code=400,
                detail="Erro ao criar cliente"
            )
        
        return {"success": True, "message": "Cliente criado com sucesso", "id": new_client.id}
        
    except Exception as e:
        logger.error(f"Erro ao criar cliente: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno")


@router.put("/clients/{client_id}")
async def update_client(
    client_id: str,
    client_update: ClientUpdate,
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Atualiza cliente existente"""
    try:
        clients_col = await get_clients_collection()
        
        update_data = {k: v for k, v in client_update.dict().items() if v is not None}
        update_data["updatedAt"] = datetime.utcnow()
        
        result = await clients_col.update_one(
            {"id": client_id},
            {"$set": update_data}
        )
        
        if result.modified_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Cliente não encontrado"
            )
        
        return {"success": True, "message": "Cliente atualizado com sucesso"}
        
    except Exception as e:
        logger.error(f"Erro ao atualizar cliente: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno")


@router.delete("/clients/{client_id}")
async def delete_client(
    client_id: str,
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Remove cliente"""
    try:
        clients_col = await get_clients_collection()
        
        result = await clients_col.delete_one({"id": client_id})
        
        if result.deleted_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Cliente não encontrado"
            )
        
        return {"success": True, "message": "Cliente removido com sucesso"}
        
    except Exception as e:
        logger.error(f"Erro ao remover cliente: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno")


@router.get("/messages")
async def get_messages(
    page: int = 1,
    limit: int = 20,
    read: Optional[bool] = None,
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Lista mensagens de contato"""
    try:
        messages_col = await get_messages_collection()
        
        # Filtros
        filter_query = {}
        if read is not None:
            filter_query["read"] = read
        
        # Paginação
        skip = (page - 1) * limit
        
        messages = await messages_col.find(filter_query)\
            .sort("createdAt", -1)\
            .skip(skip)\
            .limit(limit)\
            .to_list(limit)
        
        total = await messages_col.count_documents(filter_query)
        
        return {
            "messages": [ContactMessage(**msg) for msg in messages],
            "total": total,
            "page": page,
            "pages": (total + limit - 1) // limit
        }
        
    except Exception as e:
        logger.error(f"Erro ao buscar mensagens: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno")


@router.put("/messages/{message_id}")
async def update_message(
    message_id: str,
    message_update: ContactMessageUpdate,
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Atualiza status da mensagem"""
    try:
        messages_col = await get_messages_collection()
        
        update_data = {k: v for k, v in message_update.dict().items() if v is not None}
        
        result = await messages_col.update_one(
            {"id": message_id},
            {"$set": update_data}
        )
        
        if result.modified_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Mensagem não encontrada"
            )
        
        return {"success": True, "message": "Mensagem atualizada com sucesso"}
        
    except Exception as e:
        logger.error(f"Erro ao atualizar mensagem: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno")


# Função para criar admin padrão
async def create_default_admin():
    """Cria usuário admin padrão se não existir"""
    try:
        admin_col = await get_admin_collection()
        existing_admin = await admin_col.find_one({"username": "admin"})
        
        if not existing_admin:
            config = get_config()
            admin_data = config["admin"]
            
            default_admin = AdminUser(
                username=admin_data["default_username"],
                email=admin_data["default_email"],
                passwordHash=hash_password(admin_data["default_password"])
            )
            
            await admin_col.insert_one(default_admin.dict())
            logger.info("Admin padrão criado: username=admin, password=admin123")
        
    except Exception as e:
        logger.error(f"Erro ao criar admin padrão: {str(e)}")