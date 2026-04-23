from SRC.Utils.dbutils import base
from sqlalchemy import Column,VARCHAR,Integer
class User(base):
    __tablename__="Users_News"
    name=Column(VARCHAR(20),nullable=False)
    id=Column(Integer,autoincrement=True,primary_key=True)
    email=Column(VARCHAR(25),nullable=False)
    hash_pass=Column(VARCHAR(500),nullable=False)
     