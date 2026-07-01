from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):  #Receives data from the user
    image_url: str
    title: str
    content: str
    creator: str

class PostDisplay(BaseModel): # sends data back to user
    int: int
    image_url: str
    title: str
    content: str
    creator: str
    timestamp: datetime
    class Config(): # inner class
        orm_mode = True #DbPost->orm_mode->True->PostDisplay->convert to JSON response