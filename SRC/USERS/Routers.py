from fastapi import APIRouter,Depends,BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from SRC.USERS.Models import user,register,login
from SRC.Utils.dbutils import get_db
from SRC.USERS.Service import gets,gets2,ver
router=APIRouter(prefix="/users")

@router.post("/register")
async def all(data:register,dba:AsyncSession=Depends(get_db)):
    return await gets2(data,dba)

@router.post("/login",response_model=(user))
async def sef(data:login,dba:AsyncSession=Depends(get_db)):
    return await gets(data,dba,BackgroundTasks())

@router.post("/{email1}/{otp}")
async def votp(otp:int,email1:str):
    return  ver(email=email1,otp=otp)