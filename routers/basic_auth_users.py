from fastapi import APIRouter
from pydantic import BaseModel

class User(BaseModel):
    user_name:str
    full_name:str
    email:str
    disabled:bool

user_db={
         "WithoutS":
           {
             "user_name":"WithoutS",
             "full_name":"Marco Fernandez",
             "email":"marcoeze4@gmail.com",
             "disabled":False ,    
             "password":"12345"  
           },
         "WithoutS2":
           {
             "user_name":"WithoutS2",
             "full_name":"Marco Fernandez",
             "email":"marcoeze4@gmail.com",
             "disabled":True ,    
             "password":"54321"  
           }           
        }