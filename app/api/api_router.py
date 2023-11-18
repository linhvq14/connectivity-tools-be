from fastapi import APIRouter

from app.api import api_download, api_healthcheck

router = APIRouter()

router.include_router(api_healthcheck.router, tags=["health-check"], prefix="/healthcheck")
router.include_router(api_download.router, tags=["download"], prefix="/download")

