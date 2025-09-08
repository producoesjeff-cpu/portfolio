#!/usr/bin/env python3
"""
Script para popular o banco de dados com dados iniciais
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from pathlib import Path

# Carregar variáveis de ambiente
ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Conectar ao MongoDB
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ.get('DB_NAME', 'gaffer_portfolio')]

async def populate_projects():
    """Popular projetos"""
    projects = [
        {
            "id": "proj_1",
            "title": "Série Netflix Original",
            "client": "Netflix",
            "year": "2024",
            "category": "Série",
            "description": "Iluminação principal para série dramática de 8 episódios",
            "image": "https://images.unsplash.com/photo-1619473667737-b3abeb860aa1?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzB8MHwxfHNlYXJjaHw0fHxjaW5lbWF0b2dyYXBoeXxlbnwwfHx8fDE3NTcyOTAxOTJ8MA&ixlib=rb-4.1.0&q=85",
            "featured": True,
            "videoUrl": "",
            "createdAt": "2024-01-15T00:00:00Z",
            "updatedAt": "2024-01-15T00:00:00Z"
        },
        {
            "id": "proj_2",
            "title": "Campanha Seara",
            "client": "Seara",
            "year": "2024",
            "category": "Publicidade",
            "description": "Direção de fotografia e iluminação para campanha nacional",
            "image": "https://images.unsplash.com/photo-1625690303837-654c9666d2d0?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzB8MHwxfHNlYXJjaHwyfHxjaW5lbWF0b2dyYXBoeXxlbnwwfHx8fDE3NTcyOTAxOTJ8MA&ixlib=rb-4.1.0&q=85",
            "featured": True,
            "videoUrl": "",
            "createdAt": "2024-02-01T00:00:00Z",
            "updatedAt": "2024-02-01T00:00:00Z"
        },
        {
            "id": "proj_3",
            "title": "Documentário MIO",
            "client": "MIO",
            "year": "2023",
            "category": "Documentário",
            "description": "Iluminação natural e artificial para documentário institucional",
            "image": "https://images.unsplash.com/photo-1490971774356-7fac993cc438?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzF8MHwxfHNlYXJjaHwxfHxmaWxtJTIwbGlnaHRpbmd8ZW58MHx8fHwxNzU3MjkwMTk3fDA&ixlib=rb-4.1.0&q=85",
            "featured": True,
            "videoUrl": "",
            "createdAt": "2023-12-10T00:00:00Z",
            "updatedAt": "2023-12-10T00:00:00Z"
        },
        {
            "id": "proj_4",
            "title": "Comercial Nutrata",
            "client": "Nutrata",
            "year": "2023",
            "category": "Comercial",
            "description": "Setup de iluminação complexo para produto alimentício",
            "image": "https://images.unsplash.com/photo-1611784728558-6c7d9b409cdf?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzB8MHwxfHNlYXJjaHwzfHxjaW5lbWF0b2dyYXBoeXxlbnwwfHx8fDE3NTcyOTAxOTJ8MA&ixlib=rb-4.1.0&q=85",
            "featured": True,
            "videoUrl": "",
            "createdAt": "2023-11-20T00:00:00Z",
            "updatedAt": "2023-11-20T00:00:00Z"
        },
        {
            "id": "proj_5",
            "title": "Freboy - Videoclipe",
            "client": "Freboy",
            "year": "2024",
            "category": "Videoclipe",
            "description": "Iluminação criativa com neon e LED para videoclipe",
            "image": "https://images.pexels.com/photos/3379934/pexels-photo-3379934.jpeg",
            "featured": False,
            "videoUrl": "",
            "createdAt": "2024-01-15T00:00:00Z",
            "updatedAt": "2024-01-15T00:00:00Z"
        },
        {
            "id": "proj_6",
            "title": "Maturatta - Institutional",
            "client": "Maturatta",
            "year": "2024",
            "category": "Institucional",
            "description": "Vídeo corporativo com iluminação natural e técnica",
            "image": "https://images.pexels.com/photos/3379942/pexels-photo-3379942.jpeg",
            "featured": False,
            "videoUrl": "",
            "createdAt": "2024-02-20T00:00:00Z",
            "updatedAt": "2024-02-20T00:00:00Z"
        }
    ]
    
    await db.projects.delete_many({})  # Limpar existentes
    await db.projects.insert_many(projects)
    print(f"Inseridos {len(projects)} projetos")

async def populate_clients():
    """Popular clientes"""
    clients = [
        {
            "id": "client_1",
            "name": "Netflix",
            "logo": "/api/placeholder/120/60",
            "website": "https://netflix.com",
            "order": 1,
            "active": True,
            "createdAt": "2024-01-01T00:00:00Z",
            "updatedAt": "2024-01-01T00:00:00Z"
        },
        {
            "id": "client_2",
            "name": "MIO",
            "logo": "/api/placeholder/120/60",
            "website": "#",
            "order": 2,
            "active": True,
            "createdAt": "2024-01-01T00:00:00Z",
            "updatedAt": "2024-01-01T00:00:00Z"
        },
        {
            "id": "client_3",
            "name": "Seara",
            "logo": "/api/placeholder/120/60",
            "website": "#",
            "order": 3,
            "active": True,
            "createdAt": "2024-01-01T00:00:00Z",
            "updatedAt": "2024-01-01T00:00:00Z"
        },
        {
            "id": "client_4",
            "name": "Nutrata",
            "logo": "/api/placeholder/120/60",
            "website": "#",
            "order": 4,
            "active": True,
            "createdAt": "2024-01-01T00:00:00Z",
            "updatedAt": "2024-01-01T00:00:00Z"
        },
        {
            "id": "client_5",
            "name": "Freboy",
            "logo": "/api/placeholder/120/60",
            "website": "#",
            "order": 5,
            "active": True,
            "createdAt": "2024-01-01T00:00:00Z",
            "updatedAt": "2024-01-01T00:00:00Z"
        },
        {
            "id": "client_6",
            "name": "Maturatta",
            "logo": "/api/placeholder/120/60",
            "website": "#",
            "order": 6,
            "active": True,
            "createdAt": "2024-01-01T00:00:00Z",
            "updatedAt": "2024-01-01T00:00:00Z"
        }
    ]
    
    await db.clients.delete_many({})  # Limpar existentes
    await db.clients.insert_many(clients)
    print(f"Inseridos {len(clients)} clientes")

async def main():
    """Função principal"""
    print("Populando banco de dados...")
    
    try:
        await populate_projects()
        await populate_clients()
        print("✅ Banco de dados populado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao popular banco: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(main())