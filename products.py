from fastapi import FastAPI
 
app =FastAPI()
@app.get("/product")
async def product():
    return["Producto 1","Producto 2","Producto 3", "Producto 4", "Producto 5"]