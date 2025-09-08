import os
from typing import Dict, Any

def get_config() -> Dict[str, Any]:
    """
    Retorna configurações da aplicação
    """
    return {
        # MongoDB
        "mongo_url": os.environ.get("MONGO_URL", ""),
        "db_name": os.environ.get("DB_NAME", "gaffer_portfolio"),
        
        # JWT
        "jwt_secret": os.environ.get("JWT_SECRET_KEY", "gaffer-portfolio-secret-key-2024"),
        
        # EmailJS
        "emailjs": {
            "service_id": os.environ.get("EMAILJS_SERVICE_ID", "service_xc7jjjk"),
            "template_id": os.environ.get("EMAILJS_TEMPLATE_ID", ""),
            "user_id": os.environ.get("EMAILJS_USER_ID", ""),
            "notification_template": os.environ.get("EMAILJS_NOTIFICATION_TEMPLATE", "")
        },
        
        # Cloudinary
        "cloudinary": {
            "cloud_name": os.environ.get("CLOUDINARY_CLOUD_NAME", ""),
            "api_key": os.environ.get("CLOUDINARY_API_KEY", ""),
            "api_secret": os.environ.get("CLOUDINARY_API_SECRET", "")
        },
        
        # Admin
        "admin": {
            "default_username": os.environ.get("ADMIN_USERNAME", "admin"),
            "default_email": os.environ.get("ADMIN_EMAIL", "jeferson@exemplo.com"),
            "default_password": os.environ.get("ADMIN_PASSWORD", "admin123")
        }
    }

def validate_config() -> Dict[str, bool]:
    """
    Valida se todas as configurações necessárias estão presentes
    """
    config = get_config()
    
    return {
        "mongodb": bool(config["mongo_url"]),
        "emailjs_basic": bool(config["emailjs"]["service_id"]),
        "emailjs_complete": all([
            config["emailjs"]["service_id"],
            config["emailjs"]["template_id"],
            config["emailjs"]["user_id"]
        ]),
        "cloudinary": all([
            config["cloudinary"]["cloud_name"],
            config["cloudinary"]["api_key"],
            config["cloudinary"]["api_secret"]
        ])
    }