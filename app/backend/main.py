from fastapi import FastAPI

from app.backend.api.profile import router as profile_router

from app.backend.api.skills import router as skills_router

app = FastAPI(
    title="Enterprise Zero-Downtime CI/CD Platform",
    version="1.0.0",
)

app.include_router(
    profile_router,
    prefix="/api",
    tags=["Profile"]
)
app.include_router(
    skills_router,
    prefix="/api",
    tags=["Skills"]
)
