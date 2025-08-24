from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from models.user import User

app = FastAPI()

@app.get("/greet")
def greet(name: str = Query(..., description="Your name")):
    return JSONResponse(content={"message": f"Hello, {name}!"})

@app.get("/health")
def health():
    return JSONResponse(content={"status": "OK"})

@app.post("/users/")
def create_user(user: User):
    return JSONResponse(content={ "user": user.dict() })