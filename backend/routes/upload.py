from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Dict, Any
import logging

from services.upload import upload_image, upload_video, get_upload_config, delete_file
from routes.admin import get_current_admin
from models.admin import AdminUser

logger = logging.getLogger(__name__)
router = APIRouter()
security = HTTPBearer()


@router.get("/config")
async def upload_config():
    """Retorna configuração de upload"""
    return get_upload_config()


@router.post("/image")
async def upload_image_endpoint(
    file: UploadFile = File(...),
    folder: str = "gaffer-portfolio",
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Upload de imagem"""
    try:
        if not file:
            raise HTTPException(status_code=400, detail="Nenhum arquivo enviado")
        
        # Upload da imagem
        image_url = await upload_image(file, folder)
        
        logger.info(f"Imagem uploaded por {current_admin.username}: {image_url}")
        
        return {
            "success": True,
            "message": "Imagem enviada com sucesso",
            "url": image_url,
            "filename": file.filename
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro no upload de imagem: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro no upload da imagem")


@router.post("/video")
async def upload_video_endpoint(
    file: UploadFile = File(...),
    folder: str = "gaffer-portfolio/videos",
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Upload de vídeo"""
    try:
        if not file:
            raise HTTPException(status_code=400, detail="Nenhum arquivo enviado")
        
        # Upload do vídeo
        video_url = await upload_video(file, folder)
        
        logger.info(f"Vídeo uploaded por {current_admin.username}: {video_url}")
        
        return {
            "success": True,
            "message": "Vídeo enviado com sucesso",
            "url": video_url,
            "filename": file.filename
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro no upload de vídeo: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro no upload do vídeo")


@router.delete("/file")
async def delete_file_endpoint(
    file_url: str,
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Remove arquivo do storage"""
    try:
        success = await delete_file(file_url)
        
        if success:
            logger.info(f"Arquivo removido por {current_admin.username}: {file_url}")
            return {
                "success": True,
                "message": "Arquivo removido com sucesso"
            }
        else:
            return {
                "success": False,
                "message": "Arquivo não encontrado ou erro na remoção"
            }
        
    except Exception as e:
        logger.error(f"Erro ao remover arquivo: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao remover arquivo")


@router.post("/multiple")
async def upload_multiple_files(
    files: list[UploadFile] = File(...),
    folder: str = "gaffer-portfolio",
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Upload múltiplo de arquivos"""
    try:
        if not files:
            raise HTTPException(status_code=400, detail="Nenhum arquivo enviado")
        
        if len(files) > 10:
            raise HTTPException(status_code=400, detail="Máximo 10 arquivos por vez")
        
        results = []
        
        for file in files:
            try:
                # Determinar tipo de upload baseado no content_type
                if file.content_type.startswith("image/"):
                    url = await upload_image(file, folder)
                elif file.content_type.startswith("video/"):
                    url = await upload_video(file, f"{folder}/videos")
                else:
                    results.append({
                        "filename": file.filename,
                        "success": False,
                        "error": "Tipo de arquivo não suportado"
                    })
                    continue
                
                results.append({
                    "filename": file.filename,
                    "success": True,
                    "url": url
                })
                
            except Exception as e:
                results.append({
                    "filename": file.filename,
                    "success": False,
                    "error": str(e)
                })
        
        success_count = sum(1 for r in results if r["success"])
        
        logger.info(f"Upload múltiplo por {current_admin.username}: {success_count}/{len(files)} sucessos")
        
        return {
            "success": success_count > 0,
            "message": f"{success_count} de {len(files)} arquivos enviados com sucesso",
            "results": results
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro no upload múltiplo: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro no upload múltiplo")