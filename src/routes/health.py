from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "healthy"}

@router.get("/greet")
def greet(name: str = "World"):
    return {"message": f"Hello, {name}!"}
