# Step 09 - Project Refactoring

# Objective

Convert a single-file FastAPI application into a modular project.

---

# Why Refactor?

Small projects can live in one file.

Production projects cannot.

As applications grow:

- More APIs
- More models
- More business logic
- More configuration

Keeping everything in one file becomes difficult.

---

# New Structure

api/

Contains API routes.

models/

Contains Pydantic models.

services/

Contains business logic.

core/

Contains configuration.

main.py

Starts the application.

---

# Benefits

- Easier maintenance
- Easier testing
- Easier scaling
- Cleaner code
- Professional project structure

---

# Interview Question

Why separate business logic from API routes?

Because routes should only receive requests and return responses.

Business logic belongs in service classes so it can be reused and tested.

---

# Summary

A modular project is easier to maintain than a single large file.
