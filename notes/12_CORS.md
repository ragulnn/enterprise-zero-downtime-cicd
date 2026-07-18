# Step 12 - CORS

## What is CORS?

CORS stands for Cross-Origin Resource Sharing.

It is a browser security feature.

The browser blocks requests from one origin to another unless the server explicitly allows them.

Example

Frontend

http://localhost:3000

↓

Backend

http://127.0.0.1:8000

These are different origins.

Without CORS:

❌ Request blocked

With CORS:

✅ Request allowed

---

## FastAPI Solution

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Interview Question

Why do we use CORS?

To allow trusted frontend applications to communicate with backend APIs while preventing unauthorized websites from making requests.
