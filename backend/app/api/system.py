from fastapi import APIRouter
from app.core.config import settings

router = APIRouter(tags=["System"])


@router.get("/health")
def health():
    return {"status": "healthy"}


@router.get("/ready")
def ready():
    return {"status": "ready"}


@router.get("/version")
def version():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
    }
