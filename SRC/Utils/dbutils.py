from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from SRC.Utils.model import Setting
mas=Setting()
engine=create_async_engine(mas.db_url,pool_size=10,
                           pool_timeout=60,
                           max_overflow=20,
                           pool_recycle=1800
                           )
base=declarative_base()
localsession=sessionmaker(bind=engine,class_=AsyncSession,expire_on_commit=True)
async def get_db():
    async with localsession() as db:
        yield db