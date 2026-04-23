from pydantic import BaseModel,EmailStr

class user(BaseModel):
    name:str
    id:int
    email:EmailStr
    class config():
        from_attributes:True


class login(BaseModel):
    emai:EmailStr
    password:str

class register(BaseModel):
    name:str
    emai:EmailStr
    password:str
    