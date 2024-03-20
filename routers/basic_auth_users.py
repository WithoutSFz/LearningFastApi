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
def user_search(username:str):
    if username in user_db:
        return UserDB(user_db[username])
    
async def current_user(token:str=Depends(oauth2)):
    user = user_search(token)
    if not user :
        raise HTTPException( status_code=401, detail="Credencial de autenticacion invalida")
    return user
    
@app.post("/login")
async def login(form:OAuth2PasswordRequestForm= Depends()):
    user_db = user_db.get(form.username)
    if not user_db:
        raise HTTPException( 
             status_code=400, detail="El usuario no es correcta")
    user = user_search(form.password)
    if not form.password == user.password:
        raise HTTPException( status_code=400, detail="La contraseña no es correcta")

    return {"acces_token":user.username,"token_type":"bearer"}    

@app.get("/user/me")
async def me(user:User= Depends(current_user())):
    return user
