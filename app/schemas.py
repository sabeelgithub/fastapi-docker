from pydantic import BaseModel

class UserBase(BaseModel):
    name:str
    age:int