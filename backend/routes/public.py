from fastapi import APIRouter, HTTPException, status
from typing import List, Dict, Any
import logging

from models.portfolio import Portfolio
from models.project import Project
from models.client import Client
from models.message import ContactMessage, ContactMessageCreate
from utils.database import (
    get_portfolio_collection, 
    get_projects_collection, 
    get_clients_collection,
    get_messages_collection
)
from services.email import send_contact_email, send_admin_notification

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/")
async def api_status():
    """Status da API pública"""
    return {"message": "Gaffer Portfolio API - Jeferson Rodrigues", "status": "online"}


@router.get("/portfolio")
async def get_portfolio_data():
    """
    Retorna dados completos do portfólio para o frontend
    """
    try:
        # Collections
        portfolio_col = await get_portfolio_collection()
        projects_col = await get_projects_collection()
        clients_col = await get_clients_collection()
        
        # Buscar dados do portfólio
        portfolio_data = await portfolio_col.find_one()
        if not portfolio_data:
            # Retornar dados padrão se não existir
            portfolio_data = await create_default_portfolio()
        
        # Buscar projetos em destaque
        featured_projects = await projects_col.find(
            {"featured": True}
        ).sort("createdAt", -1).to_list(10)
        
        # Buscar projetos recentes
        recent_projects = await projects_col.find(
            {"featured": False}
        ).sort("createdAt", -1).to_list(10)
        
        # Buscar clientes ativos
        clients = await clients_col.find(
            {"active": True}
        ).sort("order", 1).to_list(20)
        
        # Formatar resposta
        response = {
            "personal": portfolio_data.get("personal", {}),
            "demoReel": portfolio_data.get("demoReel", {}),
            "services": portfolio_data.get("services", []),
            "featuredWorks": [format_project(p) for p in featured_projects],
            "recentProjects": [format_project(p) for p in recent_projects],
            "clients": [format_client(c) for c in clients]
        }
        
        return response
        
    except Exception as e:
        logger.error(f"Erro ao buscar portfólio: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Erro interno do servidor"
        )


@router.post("/contact")
async def send_contact_message(message: ContactMessageCreate):
    """
    Recebe e processa mensagem de contato
    """
    try:
        # Criar objeto de mensagem
        contact_message = ContactMessage(**message.dict())
        
        # Salvar no banco
        messages_col = await get_messages_collection()
        result = await messages_col.insert_one(contact_message.dict())
        
        if not result.inserted_id:
            raise HTTPException(
                status_code=500,
                detail="Erro ao salvar mensagem"
            )
        
        # Enviar email
        email_sent = await send_contact_email(contact_message)
        
        # Enviar notificação para admin (opcional)
        await send_admin_notification(contact_message)
        
        logger.info(f"Mensagem de contato recebida de {message.email}")
        
        return {
            "success": True,
            "message": "Mensagem enviada com sucesso! Entrarei em contato em breve.",
            "email_sent": email_sent
        }
        
    except Exception as e:
        logger.error(f"Erro ao processar contato: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Erro ao enviar mensagem. Tente novamente."
        )


# Funções auxiliares
def format_project(project: dict) -> dict:
    """Formata projeto para resposta da API"""
    return {
        "id": project.get("id"),
        "title": project.get("title"),
        "client": project.get("client"),
        "year": project.get("year"),
        "category": project.get("category"),
        "description": project.get("description"),
        "image": project.get("image", ""),
        "featured": project.get("featured", False),
        "videoUrl": project.get("videoUrl", ""),
        "date": project.get("date")
    }


def format_client(client: dict) -> dict:
    """Formata cliente para resposta da API"""
    return {
        "id": client.get("id"),
        "name": client.get("name"),
        "logo": client.get("logo", ""),
        "website": client.get("website", "")
    }


async def create_default_portfolio():
    """Cria portfólio padrão se não existir"""
    try:
        portfolio_col = await get_portfolio_collection()
        
        default_portfolio = {
            "personal": {
                "name": "Jeferson Rodrigues",
                "role": "Gaffer | Iluminação Audiovisual",
                "location": "São Paulo & Rio de Janeiro",
                "email": "jeferson@exemplo.com",
                "phone": "+55 11 9999-9999",
                "bio": "Profissional especializado em iluminação para produções audiovisuais com mais de 8 anos de experiência. Trabalho como Gaffer em grandes produções para Netflix, canais de TV e campanhas publicitárias.",
                "heroImage": "",
                "aboutImage": "",
                "social": {
                    "instagram": "@jefersonrodrigues",
                    "linkedin": "jeferson-rodrigues",
                    "youtube": "@jefersonrodrigues",
                    "whatsapp": "5511999999999"
                }
            },
            "demoReel": {
                "title": "Demo Reel 2024",
                "description": "Principais trabalhos em iluminação cinematográfica",
                "videoUrl": "",
                "thumbnail": ""
            },
            "services": [
                {
                    "title": "Gaffer",
                    "description": "Direção de iluminação para cinema, TV e publicidade",
                    "icon": "lightbulb"
                },
                {
                    "title": "Direção de Fotografia",
                    "description": "Conceito visual e estética cinematográfica",
                    "icon": "camera"
                },
                {
                    "title": "Consultoria Técnica",
                    "description": "Planejamento de equipamentos e orçamentos",
                    "icon": "settings"
                },
                {
                    "title": "Color Grading",
                    "description": "Finalização e correção de cor",
                    "icon": "palette"
                }
            ]
        }
        
        # Inserir no banco
        await portfolio_col.insert_one(default_portfolio)
        logger.info("Portfólio padrão criado")
        
        return default_portfolio
        
    except Exception as e:
        logger.error(f"Erro ao criar portfólio padrão: {str(e)}")
        return {}