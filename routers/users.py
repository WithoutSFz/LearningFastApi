from fastapi import APIRouter
from pydantic import BaseModel
router= APIRouter(prefix="/users",
                  tags=["users"])

class User(BaseModel):
    id:int
    name:str
    surname:str
    url:str
    age:int

users_list =[User(id=1,name= "Marco",surname= "Fernandez",url="http:\\marco.com",age=24),
             User(id=2,name= "Marco2",surname= "Fernandez",url="http:\\marco.com",age=24),
             User(id=3,name= "Marco3",surname= "Fernandez",url="http:\\marco.com",age=24)]
@router.get("/")
async def usersclass():
    return users_list    

def search_user(id:id):
    users=filter(lambda user:user.id==id,users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}
    
@router.get("/{id}")
async def user(id:int):
     return search_user(id)

@router.get("/")
async def userquery(id:int):
     return search_user(id)
    
@router.post("/")
async def user(user:User):
    if (type(search_user(user.id))==User):
         return {"Error":"El usuario ya existe."}
    else:
         users_list.routerend(user)
@router.put("/")
async def user(user:User):
    
     found=False
  
     for index, saved_users in enumerate(users_list):
         if(user.id==saved_users.id):
             users_list[index]=user
             found = True
     
     if  not found:
         return {"Error":"Usuario no encontrado."}
    
@router.delete("/")
async def user(user:User):
    
     found=False
  
     for index, saved_users in enumerate(users_list):
         if(user.id==saved_users.id):
             del users_list[index]
             found = True
     
     if  not found:
         return {"Error":"Usuario no eliminado."}