from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

app =FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    user_name:str
    full_name:str
    email:str
    disabled:bool

class UserDB(User):
    password:str

users_db={
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
def user_search(username:str):
    if username in users_db:
        return User(**users_db[username])
    
async def current_user(token:str=Depends(oauth2)):
    user = user_search(token)
    if not user :
        raise HTTPException( status_code=401, detail="Credencial de autenticacion invalida")
    if user.disabled:
        raise HTTPException( 
             status_code=400, detail="El usuario no esta activo")
    return user
    
@app.post("/login")
async def login(form:OAuth2PasswordRequestForm= Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException( 
             status_code=400, detail="El usuario no es correcto")   
    user = user_search(form.username)
    if not form.password == user.password:
        raise HTTPException( status_code=400, detail="La contraseña no es correcta")

    return {"acces_token":user.user_name,"token_type":"bearer"}    

@app.get("/users/me")
async def me(user:User= Depends(current_user)):
    return user
