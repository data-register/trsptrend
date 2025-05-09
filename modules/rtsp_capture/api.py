"""
API маршрути за RTSP capture модул
"""

import os
import time
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse, Response, JSONResponse, FileResponse
from fastapi.templating import Jinja2Templates

from .config import get_capture_config, update_capture_config
from .capture import capture_frame, get_placeholder_image
from utils.logger import setup_logger

# Инициализиране на логър
logger = setup_logger("rtsp_api")

# Регистриране на API router
router = APIRouter()

# Настройване на шаблони (ако има нужда)
templates_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "templates")
templates = Jinja2Templates(directory=templates_dir)

@router.get("/", response_class=HTMLResponse)
async def rtsp_index(request: Request):
    """Страница за RTSP модула"""
    config = get_capture_config()
    
    return templates.TemplateResponse("rtsp_index.html", {
        "request": request,
        "config": config,
        "timestamp": int(time.time()),
        "last_update": config.last_frame_time.strftime("%H:%M:%S") if config.last_frame_time else "Няма",
        "status": config.status,
        "status_text": "OK" if config.status == "ok" else "Грешка" if config.status == "error" else "Инициализация"
    })

@router.get("/latest.jpg")
async def latest_jpg():
    """Връща последния запазен JPEG файл"""
    try:
        config = get_capture_config()
        latest_path = os.path.join(config.save_dir, "latest.jpg")
        
        if not os.path.exists(latest_path):
            # Връщаме placeholder изображение
            return Response(content=get_placeholder_image(), media_type="image/jpeg")
        
        return FileResponse(latest_path, media_type="image/jpeg")
    except Exception as e:
        logger.error(f"Грешка при достъпване на последния кадър: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/info")
async def rtsp_info():
    """Връща информация за последния запазен кадър"""
    config = get_capture_config()
    
    if config.last_frame_time is None:
        return JSONResponse({
            "status": "no_frame",
            "message": "Все още няма запазен кадър"
        }, status_code=404)
    
    return JSONResponse({
        "status": config.status,
        "last_frame_time": config.last_frame_time.isoformat() if config.last_frame_time else None,
        "last_frame_path": config.last_frame_path,
        "rtsp_url": config.rtsp_url,
        "interval": config.interval,
        "latest_url": "/rtsp/