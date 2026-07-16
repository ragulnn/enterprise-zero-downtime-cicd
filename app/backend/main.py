from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Zero Downtime CI/CD Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Enterprise Zero Downtime CI/CD Platform"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/ready")
def ready():
    return {
        "status": "ready"
    }


@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }
