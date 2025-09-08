import os
import requests
import logging
from typing import Dict, Any
from models.message import ContactMessage

logger = logging.getLogger(__name__)

# Configurações EmailJS
EMAILJS_SERVICE_ID = os.environ.get("EMAILJS_SERVICE_ID", "service_xc7jjjk")
EMAILJS_TEMPLATE_ID = os.environ.get("EMAILJS_TEMPLATE_ID", "")
EMAILJS_USER_ID = os.environ.get("EMAILJS_USER_ID", "")
EMAILJS_URL = "https://api.emailjs.com/api/v1.0/email/send"

async def send_contact_email(message: ContactMessage) -> bool:
    """
    Envia email de contato usando EmailJS
    """
    try:
        # Dados para o template do EmailJS
        template_params = {
            "from_name": message.name,
            "from_email": message.email,
            "phone": message.phone or "Não informado",
            "subject": message.subject,
            "message": message.message,
            "to_name": "Jeferson Rodrigues",
            "reply_to": message.email
        }
        
        # Payload para EmailJS
        payload = {
            "service_id": EMAILJS_SERVICE_ID,
            "template_id": EMAILJS_TEMPLATE_ID,
            "user_id": EMAILJS_USER_ID,
            "template_params": template_params
        }
        
        # Headers
        headers = {
            "Content-Type": "application/json"
        }
        
        # Fazer requisição para EmailJS
        response = requests.post(EMAILJS_URL, json=payload, headers=headers)
        
        if response.status_code == 200:
            logger.info(f"Email enviado com sucesso para {message.email}")
            return True
        else:
            logger.error(f"Erro ao enviar email: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        logger.error(f"Erro ao enviar email: {str(e)}")
        return False

async def send_admin_notification(message: ContactMessage) -> bool:
    """
    Envia notificação para o admin sobre nova mensagem
    """
    try:
        # Template params para notificação do admin
        template_params = {
            "admin_name": "Jeferson",
            "client_name": message.name,
            "client_email": message.email,
            "client_phone": message.phone or "Não informado",
            "subject": message.subject,
            "message": message.message,
            "date": message.createdAt.strftime("%d/%m/%Y às %H:%M")
        }
        
        # Usar template de notificação (se configurado)
        notification_template = os.environ.get("EMAILJS_NOTIFICATION_TEMPLATE", EMAILJS_TEMPLATE_ID)
        
        payload = {
            "service_id": EMAILJS_SERVICE_ID,
            "template_id": notification_template,
            "user_id": EMAILJS_USER_ID,
            "template_params": template_params
        }
        
        headers = {
            "Content-Type": "application/json"
        }
        
        response = requests.post(EMAILJS_URL, json=payload, headers=headers)
        
        if response.status_code == 200:
            logger.info("Notificação enviada para admin")
            return True
        else:
            logger.warning(f"Erro ao enviar notificação admin: {response.status_code}")
            return False
            
    except Exception as e:
        logger.error(f"Erro ao enviar notificação admin: {str(e)}")
        return False

def validate_email_config() -> Dict[str, Any]:
    """
    Valida se as configurações de email estão corretas
    """
    config_status = {
        "service_id": bool(EMAILJS_SERVICE_ID),
        "template_id": bool(EMAILJS_TEMPLATE_ID),
        "user_id": bool(EMAILJS_USER_ID),
        "configured": bool(EMAILJS_SERVICE_ID and EMAILJS_TEMPLATE_ID and EMAILJS_USER_ID)
    }
    
    if not config_status["configured"]:
        logger.warning("EmailJS não está completamente configurado")
    
    return config_status