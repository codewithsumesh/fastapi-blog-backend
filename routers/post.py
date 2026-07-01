from fastapi import APIRouter,Depends,UploadFile,File
from routers.schemas import PostBase,PostDisplay
from sqlalchemy.orm import Session
from database.database import get_db
from database import db_post
import string
import random
import shutil

router = APIRouter(
    prefix ='/post',
    tags=['post']
)

@router.post('')
def create(request: PostBase,db: Session= Depends(get_db)):#non default parameters first #handles api request #Receptionist(get_db)->clerk(session)
    return db_post.create(db,request)  # function calling

@router.get('/all')
def posts(db:Session = Depends(get_db)):   
    return db_post.get_all(db)

@router.delete('/{id}')
def  delete(id:int,db: Session=Depends(get_db)):
    return db_post.delete(id,db)

@router.post('/image')
def upload_image(image: UploadFile = File(...)):
    letter = string.ascii_letters
    rand_str = ''.join(random.choice(letter) for i in range(6))  # no space is a separator
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.',1))   # new is a glue/separator imgage.jpg splits -->imgage + new + jpg
    path = f'images/{filename}'
    # python treats it as text
    with open(path, "w+b") as buffer:   # open->Create a empty file(buffer)  ,open in binary read/write mode
        shutil.copyfileobj(image.file, buffer)  # source ->copy image as bytes(binary) since its not text file-> destination buffer(now not empty)

    return {'filename': path}  #send to whoever called the api