import smtplib
import redis
from fastapi.responses import JSONResponse
from SRC.Utils.model import Setting
mas=Setting()
r=redis.Redis.from_url(mas.redis_url,decode_responses=True)
def sed(email:str,otp:int):
    print("0")
    message=f"hello there \n now stay updated with us \n welcome to relos news \n your otp is {otp} "
    x=r.get(f"{email}")
    print(x)
    try:
        if x is None:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            print("1")
            server.starttls()  # Secure connection
            print("2")
            server.login("makmish.dev@gmail.com", mas.app_pass)
            print("3")
            server.sendmail("makmish.dev@gmail.com", email, message)
            print("4")
            server.quit()
            r.set(email,otp)
            r.expire(email,60)
            print(r.get(email))
            r.expire(email,time=50)
        else:
            JSONResponse(
                status_code=433,
                content={
                    "status":"already sent"
                }
            )
            
    except Exception as e:
        print(f"Error: {e}")
    
def verify2(email: str, otp: int):
    print(r.get(email))
    print(r.get(email))
    print("upar")
    stored_otp = r.get(email)
    if stored_otp is None:
        return 2   # expired
    
    if stored_otp == str(otp):
        return 0   # success
    
    return 1       # wrong otp

