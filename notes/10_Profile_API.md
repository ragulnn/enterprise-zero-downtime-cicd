# Step 10 - Build Profile API

# Objective

Replace the demo Order API with a real Portfolio API.

Instead of returning sample order data, the backend will return profile information that the portfolio website will display.

---

# What is an API?

API stands for Application Programming Interface.

It allows two applications to communicate.

Example

Portfolio Website

↓

HTTP Request

↓

FastAPI

↓

JSON Response

---

# Why use an API?

Instead of hardcoding data in the frontend, the frontend requests data from the backend.

Advantages

- Easier updates
- Better security
- Reusable data
- Mobile apps can use the same API

---

# Endpoint

GET /api/profile

Returns

- Name
- Title
- Location
- Summary
- Skills

---

# Interview Question

Why separate frontend and backend?

The frontend focuses on displaying data while the backend manages data and business logic.

---

# Summary

The frontend will now retrieve profile information from the backend instead of storing it directly.
