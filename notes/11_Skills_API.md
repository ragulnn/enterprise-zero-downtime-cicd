# Step 11 - Skills API

## Objective

Create a dedicated API endpoint for technical skills.

---

## Why?

Instead of storing skills inside the profile endpoint, expose them through a dedicated service.

Advantages

- Easier updates
- Better separation of concerns
- Frontend can request only the data it needs

---

## Endpoint

GET /api/skills

Returns

Cloud

DevOps

Programming

Tools

---

## Interview Question

Why split APIs?

Small APIs are easier to maintain, test and reuse.
