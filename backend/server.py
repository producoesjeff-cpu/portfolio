from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
from pathlib import Path

# Importar rotas
from routes.public import router as public_router
from routes.admin import router as admin_router
from routes.upload import router as upload_router

# Importar utilitários
from utils.database import connect_to_mongo, close_mongo_connection
from utils.config import validate_config
from services.email import validate_email_config

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Iniciando Gaffer Portfolio API")
    
    # Conectar ao MongoDB
    await connect_to_mongo()
    
    # Validar configurações
    config_status = validate_config()
    email_status = validate_email_config()
    
    logger.info(f"Status das configurações: {config_status}")
    logger.info(f"Status do email: {email_status}")
    
    # Criar admin padrão se não existir
    from routes.admin import create_default_admin
    await create_default_admin()
    
    yield
    
    # Shutdown
    logger.info("Encerrando aplicação")
    await close_mongo_connection()

# Create the main app
app = FastAPI(
    title="Gaffer Portfolio API",
    description="API para portfólio profissional de Gaffer - Jeferson Rodrigues",
    version="1.0.0",
    lifespan=lifespan
)

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Incluir rotas
api_router.include_router(public_router, tags=["Public"])
api_router.include_router(admin_router, prefix="/admin", tags=["Admin"])
api_router.include_router(upload_router, prefix="/upload", tags=["Upload"])

# Include the router in the main app
app.include_router(api_router)

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota de status geral
@app.get("/")
async def root():
    return {
        "message": "Gaffer Portfolio API",
        "version": "1.0.0",
        "status": "online"
    }

# Rota de health check
@app.get("/health")
async def health_check():
    config_status = validate_config()
    email_status = validate_email_config()
    
    return {
        "status": "healthy",
        "database": config_status["mongodb"],
        "email_configured": email_status["configured"],
        "cloudinary": config_status["cloudinary"]
    }
