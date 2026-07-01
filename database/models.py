from .database import Base
from sqlalchemy import Column,Integer,String,DateTime

class DbPost(Base): #defines table strcture/blue print and talks to the database(read/write)
    __tablename__ = "post"    #__ is a special variable name Sqlalchemy looks for
    id = Column(Integer,primary_key=True,index=True)
    image_url = Column(String)
    title = Column(String)
    content = Column(String)
    creator = Column(String)
    timestamp =Column(DateTime)