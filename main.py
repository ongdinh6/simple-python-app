from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/greet")
def greet(name: str = Query(..., description="Your name")):
    return JSONResponse(content={"message": f"Hello, {name}!"})

@app.get("/health")
def health():
    return JSONResponse(content={"status": "OK"})
