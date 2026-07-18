from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.profile import router as profile_router
from app.api.skills import router as skills_router

app = FastAPI(
    title="Enterprise Portfolio API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(profile_router)
app.include_router(skills_router)


@app.get("/")
def root():
    return {"message": "Enterprise Portfolio API is running"}
