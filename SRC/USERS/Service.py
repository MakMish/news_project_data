from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException,BackgroundTasks,Depends
from sqlalchemy import select
import redis
from SRC.Utils.dbutils import get_db
from SRC.USERS.Schemas import User
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from SRC.USERS.Models import register,login
from SRC.Utils.verify import sed,verify2
import redis
import random
from SRC.Utils.model import setting
r=redis.Redis.from_url(setting.redis_url,decode_responses=True)
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
async def gets(data: login, dba: AsyncSession,bgts:BackgroundTasks):
    try:
        v=await dba.execute(select(User).where(User.email==data.emai))
        reslt=v.scalars().first()
        if reslt is None:
            raise HTTPException(status_code=438,detail="invalid")
        return {
        "id": reslt.id,
        "name": reslt.name,
        "email":reslt.email
         }
    except Exception as e:
        raise HTTPException(status_code=444,detail=f"{e}")

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
        otp = random.randint(100000, 999999)   
        sed(email=data.emai,otp=otp)
        return{
            "status":"registeration successfull"
             }
    
    except:
        raise HTTPException(status_code=429,detail="not a valid email")  

def ver(email:str,otp:int):
    try:
        print("1")
        v=verify2(email,otp)
        print("1")
        if v==2:
            raise HTTPException(status_code=410, detail="OTP expired") 
        elif v==0:
            return {
                "status": "success"
            }
        else:
            print(v)
            print("uoarr wala")
            raise HTTPException(status_code=408, detail="OTP invalid")
        

    except HTTPException:
        raise

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"{e}")
    

