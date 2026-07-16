from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Enterprise Zero Downtime CI/CD Platform",
    version="1.0.0"
)


class Order(BaseModel):
    customer: str
    product: str
    quantity: int


orders = []


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


@app.get("/orders")
def get_orders():
    return orders


@app.post("/orders")
def create_order(order: Order):
    orders.append(order)
    return {
        "message": "Order Created",
        "order": order
    }
