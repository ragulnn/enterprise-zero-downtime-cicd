# Step 05 - FastAPI Introduction

---

# Objective

In this step, we prepare the backend for our Enterprise Zero-Downtime CI/CD Platform by setting up a FastAPI project.

This backend will later be:

- Dockerized
- Stored in Azure Container Registry (ACR)
- Deployed to Azure Kubernetes Service (AKS)
- Monitored using Prometheus
- Tested using K6
- Updated using Zero-Downtime Deployments

This is the application that our CI/CD pipeline will build and deploy throughout the project.

---

# Prerequisites

Before starting this step, ensure:

- Git is installed.
- Python 3.12 or later is installed.
- Repository is cloned.
- You are inside the project root.

Check your location:

```bash
pwd
```

Expected:

```
~/enterprise-zero-downtime-cicd
```

---

# Project Structure

Current structure

```
enterprise-zero-downtime-cicd/

app/
backend/

docker/

terraform/

helm/

monitoring/

notes/

docs/
```

Backend files that will be created:

```
app/backend/

main.py

requirements.txt

README.md
```

---

# What is FastAPI?

FastAPI is a modern Python framework used to build REST APIs.

It allows developers to create web services quickly while providing excellent performance.

Architecture

```
Browser

↓

HTTP Request

↓

FastAPI

↓

Python Code

↓

HTTP Response
```

---

# Why FastAPI?

We could have used:

- Flask
- Django
- Express.js
- Spring Boot

We choose FastAPI because it provides:

- High performance
- Automatic API documentation
- Easy health endpoints
- Excellent Kubernetes integration
- Type validation
- Async support

FastAPI is widely used in cloud-native applications.

---

# What is a REST API?

A REST API allows applications to communicate over HTTP.

Example

```
Client

↓

GET /orders

↓

Server

↓

JSON Response
```

Instead of displaying web pages, APIs exchange data.

---

# Packages Used

## FastAPI

Creates the web application.

Without FastAPI, we cannot build our API.

---

## Uvicorn

Runs the FastAPI application.

Without Uvicorn:

```
Python Code

↓

Nothing happens
```

With Uvicorn:

```
Browser

↓

HTTP Request

↓

Uvicorn

↓

FastAPI

↓

Response
```

---

## Prometheus Client

Later in the project we will expose

```
/metrics
```

Prometheus will collect:

- CPU usage
- Request count
- Response time
- Error count

This package enables those metrics.

---

# Virtual Environment

We create a virtual environment so every project has its own Python packages.

Without a virtual environment:

```
Entire Computer

↓

Python Packages
```

Every project shares the same packages.

This often causes dependency conflicts.

With a virtual environment:

```
Project

↓

.venv

↓

Packages
```

Every project is isolated.

This is the recommended Python development practice.

---

# Commands Used

Create backend files

```bash
mkdir -p app/backend

touch app/backend/main.py

touch app/backend/requirements.txt

touch app/backend/README.md
```

Create virtual environment

```bash
python3 -m venv app/backend/.venv
```

Activate virtual environment

```bash
source app/backend/.venv/bin/activate
```

Install packages

```bash
pip install -r app/backend/requirements.txt
```

---

# Command Explanation

## python3

Runs Python.

---

## -m

Runs a Python module.

---

## venv

Creates a virtual environment.

---

## source

Loads the virtual environment into the current terminal.

---

## pip

Python package manager.

---

## install

Downloads packages.

---

## -r

Reads packages from a file.

---

## requirements.txt

List of required Python packages.

---

# Verification

Check Python version

```bash
python --version
```

Check installed packages

```bash
pip list
```

Check backend files

```bash
ls app/backend
```

Expected

```
main.py

requirements.txt

README.md

.venv
```

---

# Common Errors

## ReadTimeoutError

Reason

Internet connection timed out while downloading packages.

Solution

```bash
pip install --default-timeout=300 -r app/backend/requirements.txt
```

---

## Module Not Found

Reason

Virtual environment is not activated.

Solution

```bash
source app/backend/.venv/bin/activate
```

---

## Permission Denied

Reason

Using system Python instead of virtual environment.

Activate the virtual environment before installing packages.

---

# Interview Questions

## What is FastAPI?

FastAPI is a modern Python web framework used for building high-performance REST APIs.

---

## Why FastAPI instead of Flask?

FastAPI provides:

- Better performance
- Automatic API documentation
- Type validation
- Async support

---

## Why do we use a virtual environment?

A virtual environment isolates project dependencies and prevents conflicts between different Python projects.

---

## What is requirements.txt?

A file that contains all Python dependencies required for the project.

---

## What does pip install -r requirements.txt do?

It installs every package listed in requirements.txt.

---

# Summary

In this step we learned:

- What FastAPI is.
- Why we selected FastAPI.
- What a REST API is.
- Why virtual environments are important.
- What each required package does.
- How Python dependencies are installed.

This completes the backend setup preparation.

The next step will be creating our first FastAPI application and exposing production-ready endpoints.
