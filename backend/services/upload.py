import os
import cloudinary
import cloudinary.uploader
from typing import Optional
import logging
from fastapi import HTTPException, UploadFile
import uuid

logger = logging.getLogger(__name__)

# Configuração Cloudinary
cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME", ""),
    api_key=os.environ.get("CLOUDINARY_API_KEY", ""),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET", "")
)

# Tipos de arquivo permitidos
ALLOWED_IMAGE_TYPES = {
    "image/jpeg", "image/jpg", "image/png", "image/webp", "image/gif"
}

ALLOWED_VIDEO_TYPES = {
    "video/mp4", "video/avi", "video/mov", "video/wmv", "video/flv"
}

MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB

def is_cloudinary_configured() -> bool:
    """Verifica se Cloudinary está configurado"""
    return all([
        os.environ.get("CLOUDINARY_CLOUD_NAME"),
        os.environ.get("CLOUDINARY_API_KEY"),
        os.environ.get("CLOUDINARY_API_SECRET")
    ])

async def upload_image(file: UploadFile, folder: str = "gaffer-portfolio") -> str:
    """
    Upload de imagem para Cloudinary
    """
    try:
        # Validações
        if not file.content_type in ALLOWED_IMAGE_TYPES:
            raise HTTPException(
                status_code=400,
                detail="Tipo de arquivo não permitido. Use: JPG, PNG, WebP, GIF"
            )
        
        # Verificar tamanho do arquivo
        contents = await file.read()
        if len(contents) > MAX_FILE_SIZE:
            raise HTTPException(status_code=400, detail="Arquivo muito grande (máx 50MB)")
        
        # Reset file pointer
        await file.seek(0)
        
        if not is_cloudinary_configured():
            # Fallback: salvar localmente se Cloudinary não configurado
            return await save_file_locally(file, folder)
        
        # Upload para Cloudinary
        upload_result = cloudinary.uploader.upload(
            contents,
            folder=folder,
            public_id=f"{folder}_{uuid.uuid4()}",
            overwrite=True,
            resource_type="image",
            format="webp",  # Converter para WebP para otimização
            quality="auto:good",
            fetch_format="auto"
        )
        
        logger.info(f"Imagem uploaded: {upload_result['public_id']}")
        return upload_result["secure_url"]
        
    except Exception as e:
        logger.error(f"Erro no upload da imagem: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro no upload da imagem")

async def upload_video(file: UploadFile, folder: str = "gaffer-portfolio/videos") -> str:
    """
    Upload de vídeo para Cloudinary
    """
    try:
        # Validações
        if not file.content_type in ALLOWED_VIDEO_TYPES:
            raise HTTPException(
                status_code=400,
                detail="Tipo de arquivo não permitido. Use: MP4, AVI, MOV, WMV"
            )
        
        contents = await file.read()
        if len(contents) > MAX_FILE_SIZE:
            raise HTTPException(status_code=400, detail="Arquivo muito grande (máx 50MB)")
        
        await file.seek(0)
        
        if not is_cloudinary_configured():
            return await save_file_locally(file, folder)
        
        # Upload para Cloudinary
        upload_result = cloudinary.uploader.upload(
            contents,
            folder=folder,
            public_id=f"{folder}_{uuid.uuid4()}",
            overwrite=True,
            resource_type="video"
        )
        
        logger.info(f"Vídeo uploaded: {upload_result['public_id']}")
        return upload_result["secure_url"]
        
    except Exception as e:
        logger.error(f"Erro no upload do vídeo: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro no upload do vídeo")

async def save_file_locally(file: UploadFile, folder: str) -> str:
    """
    Fallback: salvar arquivo localmente quando Cloudinary não está configurado
    """
    try:
        # Criar diretório se não existir
        upload_dir = f"/app/uploads/{folder}"
        os.makedirs(upload_dir, exist_ok=True)
        
        # Nome único para o arquivo
        file_extension = file.filename.split(".")[-1] if "." in file.filename else ""
        unique_filename = f"{uuid.uuid4()}.{file_extension}"
        file_path = os.path.join(upload_dir, unique_filename)
        
        # Salvar arquivo
        contents = await file.read()
        with open(file_path, "wb") as f:
            f.write(contents)
        
        # Retornar URL local
        return f"/uploads/{folder}/{unique_filename}"
        
    except Exception as e:
        logger.error(f"Erro ao salvar arquivo localmente: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao salvar arquivo")

async def delete_file(url: str) -> bool:
    """
    Deleta arquivo do Cloudinary ou local
    """
    try:
        if "cloudinary" in url:
            # Extrair public_id da URL do Cloudinary
            public_id = url.split("/")[-1].split(".")[0]
            result = cloudinary.uploader.destroy(public_id)
            return result.get("result") == "ok"
        else:
            # Arquivo local
            if url.startswith("/uploads/"):
                file_path = f"/app{url}"
                if os.path.exists(file_path):
                    os.remove(file_path)
                    return True
        return False
        
    except Exception as e:
        logger.error(f"Erro ao deletar arquivo: {str(e)}")
        return False

def get_upload_config():
    """
    Retorna configuração de upload
    """
    return {
        "cloudinary_configured": is_cloudinary_configured(),
        "max_file_size_mb": MAX_FILE_SIZE // (1024 * 1024),
        "allowed_image_types": list(ALLOWED_IMAGE_TYPES),
        "allowed_video_types": list(ALLOWED_VIDEO_TYPES)
    }