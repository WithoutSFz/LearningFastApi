from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()

class User(BaseModel):
    id:int
    name:str
    surname:str
    url:str
    age:int

users_list =[User(id=1,name= "Marco",surname= "Fernandez",url="http:\\marco.com",age=24),
             User(id=2,name= "Marco2",surname= "Fernandez",url="http:\\marco.com",age=24),
             User(id=3,name= "Marco3",surname= "Fernandez",url="http:\\marco.com",age=24)]
@app.get("/user")
async def usersclass():
    return users_list    
@app.get("/user/{id}")
async def user(id:int):
    users=filter(lambda user:user.id==id,users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}
@app.get("/user/")
async def userquery(id:int):
    users=filter(lambda user:user.id==id,users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}