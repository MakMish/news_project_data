import smtplib
import random
import redis
from SRC.Utils.model import Setting
mas=Setting()
r=redis.Redis.from_url(mas.redis_url)
async def sed(email:str):
    print("0")
    otp=random.randint(100000,999999)
    message=f"hello there \n now stay updated with us \n welcome to relos news \n your otp is {otp} "
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        print("1")
        server.starttls()  # Secure connection
        print("2")
        server.login("makmish.dev@gmail.com", "ybey udsw hskf xeiu")
        print("3")
        server.sendmail("makmish.dev@gmail.com", email, message)
        print("4")
        server.quit()
        
        # Unique key for each user
        r.setex(f"otp:{email}", 120, str(otp))
        print(f"OTP sent to {email}")
        
    except Exception as e:
        print(f"Error: {e}")
    
def verify2(email: str, otp: int):
    stored_otp = r.get(f"otp:{email}")
    
    if stored_otp is None:
        return 2   # expired
    
    if stored_otp == str(otp):
        return 0   # success
    
    return 1       # wrong otp

