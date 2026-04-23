from fastapi import FastAPI
from SRC.USERS.Routers import router
from fastapi.middleware.cors import CORSMiddleware
from SRC.Utils.dbutils import engine,base
from SRC.AI.AI_file import res
app=FastAPI()
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(base.metadata.create_all)
app.include_router(router)
app.include_router(res)
@app.on_event("startup")
async def on_startup():
    await init_db()