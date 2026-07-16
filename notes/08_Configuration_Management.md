# Step 08 - Configuration Management

# Objective

Learn why production applications use environment variables instead of hardcoded values.

---

# What is Configuration?

Configuration is information that changes between environments without changing the application code.

Examples

- Version
- Database URL
- API Keys
- Debug Mode
- Port Number

---

# Why not hardcode?

Bad

```
DATABASE=localhost
```

Production uses a different database.

Changing the source code every time is dangerous.

Instead

```
DATABASE_URL
```

comes from the environment.

---

# Environment Variables

Environment variables are values supplied to an application when it starts.

Example

```
VERSION=1.0.0

↓

FastAPI

↓

Application
```

---

# Advantages

- No hardcoded secrets
- Easy deployment
- Different values for Dev, Stage and Prod
- Kubernetes compatible
- Docker compatible

---

# Why is this important?

Docker

↓

Container

↓

Environment Variables

↓

Application

AKS

↓

ConfigMap

↓

Environment Variables

↓

Application

---

# Commands

Create .env

touch app/backend/.env

Create configuration file

touch app/backend/config.py

---

# Interview Questions

Why use environment variables?

Because configuration changes between environments while application code stays the same.

---

What kinds of information belong in environment variables?

Database URLs, API keys, ports, feature flags and application versions.

---

# Summary

Production applications never hardcode configuration.

Environment variables make applications portable and secure.
