from fastapi import FastAPI
from src.routes import health, user

app = FastAPI()

# Include the routes
app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(user.router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
