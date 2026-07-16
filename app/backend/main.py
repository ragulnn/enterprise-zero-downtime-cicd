from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Enterprise Zero-Downtime CI/CD Platform",
    description="Production-grade FastAPI backend for demonstrating Azure DevOps, AKS, Helm, Argo Rollouts, and Zero-Downtime Deployments.",
    version="1.0.0",
)


class Order(BaseModel):
    customer: str
    product: str
    quantity: int


orders: List[Order] = []


@app.get("/", tags=["General"])
def home():
    return {
        "message": "Welcome to Enterprise Zero-Downtime CI/CD Platform",
        "service": "Order Service",
        "version": app.version,
    }


@app.get("/health", tags=["Health"])
def health():
    return {
        "status": "healthy",
        "service": "Order Service",
        "version": app.version,
    }


@app.get("/ready", tags=["Health"])
def ready():
    return {
        "status": "ready",
        "service": "Order Service",
        "version": app.version,
    }


@app.get("/version", tags=["General"])
def version():
    return {
        "version": app.version,
    }


@app.get(
    "/orders",
    response_model=List[Order],
    tags=["Orders"],
)
def get_orders():
    return orders


@app.post(
    "/orders",
    response_model=Order,
    tags=["Orders"],
)
def create_order(order: Order):
    orders.append(order)
    return order
