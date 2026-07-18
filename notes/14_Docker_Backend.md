# Step 14 - Dockerizing FastAPI

## Objective

Containerize the backend application.

Instead of running

uvicorn app.backend.main:app --reload

inside Linux,

the application will run inside a Docker container.

---

## Why Docker?

Docker packages

- Code
- Python
- Dependencies
- Environment

into one portable image.

Advantages

- Same environment everywhere
- Easy deployment
- Works on any machine
- Required for Kubernetes

---

## Flow

Source Code

↓

Docker Image

↓

Docker Container

↓

FastAPI

---

## Interview Question

Why Docker?

Docker removes the "it works on my machine" problem by packaging the application and all its dependencies into one portable container.
