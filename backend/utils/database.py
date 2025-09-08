import os
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class Database:
    client: Optional[AsyncIOMotorClient] = None
    database = None

database = Database()

async def get_database():
    """Retorna instância do banco de dados"""
    return database.database

async def connect_to_mongo():
    """Conecta ao MongoDB"""
    try:
        database.client = AsyncIOMotorClient(os.environ["MONGO_URL"])
        database.database = database.client[os.environ.get("DB_NAME", "gaffer_portfolio")]
        logger.info("Conectado ao MongoDB")
        
        # Criar índices necessários
        await create_indexes()
        
    except Exception as e:
        logger.error(f"Erro ao conectar ao MongoDB: {str(e)}")
        raise e

async def close_mongo_connection():
    """Fecha conexão com MongoDB"""
    if database.client:
        database.client.close()
        logger.info("Conexão com MongoDB fechada")

async def create_indexes():
    """Cria índices necessários no banco"""
    try:
        db = database.database
        
        # Índices para projects
        await db.projects.create_index("featured")
        await db.projects.create_index("createdAt")
        await db.projects.create_index("client")
        
        # Índices para clients
        await db.clients.create_index("active")
        await db.clients.create_index("order")
        
        # Índices para messages
        await db.messages.create_index("read")
        await db.messages.create_index("createdAt")
        
        # Índices para admin
        await db.admin_users.create_index("username", unique=True)
        await db.admin_users.create_index("email", unique=True)
        
        logger.info("Índices criados com sucesso")
        
    except Exception as e:
        logger.error(f"Erro ao criar índices: {str(e)}")

# Funções helper para collections
async def get_portfolio_collection():
    """Retorna collection do portfolio"""
    db = await get_database()
    return db.portfolio

async def get_projects_collection():
    """Retorna collection dos projetos"""
    db = await get_database()
    return db.projects

async def get_clients_collection():
    """Retorna collection dos clientes"""
    db = await get_database()
    return db.clients

async def get_messages_collection():
    """Retorna collection das mensagens"""
    db = await get_database()
    return db.messages

async def get_admin_collection():
    """Retorna collection dos admins"""
    db = await get_database()
    return db.admin_users