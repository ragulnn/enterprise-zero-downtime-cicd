from fastapi import FastAPI

from app.backend.api.profile import router as profile_router

app = FastAPI(
    title="Enterprise Zero-Downtime CI/CD Platform",
    version="1.0.0",
)

app.include_router(
    profile_router,
    prefix="/api",
    tags=["Profile"]
)
