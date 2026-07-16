# Step 07 - Order Service API

# Objective

In this step we create our first business API.

Instead of only exposing health endpoints, the application will now store and return orders.

This simulates a real backend service.

---

# Why an Order Service?

Real applications manage data.

Examples

- Orders
- Customers
- Products
- Payments

Using orders keeps the project simple while still demonstrating backend development.

---

# New Endpoints

GET /orders

Returns every order.

POST /orders

Creates a new order.

---

# Temporary Storage

For now, orders are stored in memory.

```
Application

↓

Python List

↓

Orders
```

Later we will replace this with PostgreSQL running in Kubernetes.

---

# What is JSON?

JSON is the standard format APIs use to exchange data.

Example

{
    "customer":"Alice",
    "product":"Laptop",
    "quantity":2
}

---

# HTTP Methods

GET

Retrieve data.

POST

Create data.

---

# Pydantic

FastAPI uses Pydantic for request validation.

Instead of manually checking every field, FastAPI validates requests automatically.

---

# Why are we not using a database yet?

Because our focus is CI/CD.

We'll introduce PostgreSQL later after the deployment pipeline is complete.

---

# Verification

POST

Creates a new order.

GET

Returns all orders.

---

# Interview Questions

Why use Pydantic?

It validates incoming requests and converts JSON into Python objects.

Why store data in memory?

To simplify early development before introducing a database.
