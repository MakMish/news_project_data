from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException,BackgroundTasks,Depends
from sqlalchemy import select
import redis
from SRC.Utils.dbutils import get_db
from SRC.Utils.verify import verify2
from SRC.USERS.Schemas import User
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from SRC.USERS.Models import register,login
from SRC.Utils.verify import sed
import redis
def msg(email:str):
    BackgroundTasks().add_task(sed,email)
r=redis.Redis(host="localhost",port=6379)
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
r=redis.Redis(host="localhost",port=6379,decode_responses=True)
async def gets(data: login, dba: AsyncSession):
    try:
        v=await dba.execute(select(User).where(User.email==data.emai))
        reslt=v.scalars().first()
        if reslt is None:
            raise HTTPException(status_code=438,detail="invalid")
        
        await sed(data.emai)
       
        return {
        "id": reslt.id,
        "name": reslt.name,
        "email":reslt.email
         }
    except:
        raise HTTPException(status_code=444,detail="error credentials")

async def gets2(data:register,dba:AsyncSession=Depends(get_db)):
    try:
        d=User(
        name=data.name,
        email=data.emai,
        hash_pass=pwd_context.hash(data.password)
         )
        dba.add(d)
        await dba.commit()
        await dba.refresh(d)
        return{
            "status":"registeration successfull"
             }
    except:
        raise HTTPException(status_code=429,detail="not a valid email")  

def ver (otp,email):
    try:
       v= verify2(email,otp)
       if(v==0):
           return{
               "status":"success"
           }
       else:
           raise HTTPException(status_code=409,detail="error")
    except:
        raise HTTPException(status_code=404,detail="otp not match")

