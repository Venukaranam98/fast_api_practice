from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name : str
    price : float
    in_stock : bool
@app.post("/products")
def post_products(product:Product):
    if product.price<=0:
        raise HTTPException(status_code=400,detail="Invalid price")

    return product

