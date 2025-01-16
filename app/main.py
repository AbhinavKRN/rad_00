from fastapi import FastAPI
from .routes.user import router as user_router

app = FastAPI(title="User Management API")

app.include_router(user_router, tags=["users"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)