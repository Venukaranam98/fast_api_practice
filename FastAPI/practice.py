from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()


products = {

    1: {
        "name": "Laptop",
        "price": 50000
    },

    2: {
        "name": "Shirt",
        "price": 30000
    }

}


@app.get("/products/{product_id}")

def get_product(

    product_id: int,

    discount: Optional[bool] = False


):

    if product_id not in products:

        raise HTTPException(

            status_code=404,

            detail="Product not found"

        )

    product = products[product_id]


    if discount:

        discounted_price = (

            product["price"] * 0.9

        )

        product["discounted_price"] = discounted_price


    return product