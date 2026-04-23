from fastapi import APIRouter
res=APIRouter(prefix="/ask")
from google import genai
from SRC.Utils.model import setting
from pydantic import BaseModel
class data(BaseModel):
    Text:str



client=genai.Client(api_key=setting.api_key)
@res.post("/")
def fgf(data:data):
    response=client.models.generate_content(model="gemini-2.5-flash-lite",contents=data.Text)
    return{
    "status":str(response.text)
     }
