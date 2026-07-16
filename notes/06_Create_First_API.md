# Step 06 - Create Your First FastAPI Application

---

# Objective

In this step we create our first FastAPI application.

Instead of creating a simple "Hello World" application, we will build a production-ready API that includes endpoints required by Kubernetes and monitoring tools.

---

# Why are we creating these endpoints?

Later in this project we will use:

- Docker
- Azure Kubernetes Service
- Prometheus
- Grafana
- Argo Rollouts

These tools expect our application to expose health endpoints.

Instead of rewriting the application later, we build them now.

---

# API Endpoints

| Endpoint | Purpose |
|----------|----------|
| / | Home page |
| /health | Liveness Probe |
| /ready | Readiness Probe |
| /version | Application Version |

---

# What is a Route?

A route is simply a URL that your application responds to.

Example

Browser requests

GET /

↓

FastAPI receives request

↓

Python function executes

↓

JSON response returned

---

# HTTP GET

GET requests retrieve information.

Examples

GET /

GET /orders

GET /health

GET never changes data.

---

# HTTP POST

POST requests create new data.

Example

POST /orders

We will implement POST in the next step.

---

# Liveness Probe

Purpose

Checks whether the application is still alive.

If this endpoint fails,

Kubernetes restarts the container.

---

# Readiness Probe

Purpose

Checks whether the application is ready to receive traffic.

If this endpoint fails,

Kubernetes stops sending requests to the application.

This is one of the most important features for Zero-Downtime Deployment.

---

# Version Endpoint

Purpose

Shows which application version is running.

Useful during Canary Deployments and Blue-Green Deployments.

---

# Commands Used

Run application

```bash
uvicorn main:app --reload
```

---

# Command Explanation

uvicorn

Runs the web server.

main

Python file name.

app

FastAPI object.

--reload

Automatically reloads whenever code changes.

Useful during development.

---

# Verification

Visit

http://127.0.0.1:8000

http://127.0.0.1:8000/health

http://127.0.0.1:8000/ready

http://127.0.0.1:8000/version

---

# Common Errors

ModuleNotFoundError

Usually means FastAPI is not installed.

Activate the virtual environment.

---

Address already in use

Another server is already running.

Stop it or use another port.

---

# Interview Questions

Why do Kubernetes applications expose /health?

To allow Kubernetes to determine whether the application should be restarted.

---

What is the difference between /health and /ready?

/health checks if the application is alive.

/ready checks if it is ready to receive traffic.

---

# Summary

In this step we created our first FastAPI application and exposed endpoints that will later integrate with Kubernetes, Prometheus and Argo Rollouts.
