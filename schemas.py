from pydantic import BaseModel, Field

class StudentCreate(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(gt=0, lt=100) 
    city: str = Field(min_length=2, max_length=50)

class StudentOut(BaseModel):
    id: int 
    name: str
    age:int
    city: str 
    
    class Config: 
        from_attributes = True 