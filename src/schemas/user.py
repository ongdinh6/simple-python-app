from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str | None = None