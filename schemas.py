from pydantic import BaseModel, Field

class Student(BaseModel):
    id: int
    name: str = Field(..., min_length=2)
    age: int = Field(..., gt=0)
    course: str = Field(..., min_length=2)