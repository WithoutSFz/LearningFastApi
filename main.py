from fastapi import FastAPI
from pydantic import BaseModel
from routers import products, users


app= FastAPI()
app.include_router(products.router)
app.include_router(users.router)

@app.get("/")

async def root():
    return "Hola, FastAPi"

