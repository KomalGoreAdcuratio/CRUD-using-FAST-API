
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    std: int 
    age: int 