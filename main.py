from fastapi import FastAPI, Request
from data import products
app = FastAPI()

@app.get("/")
def home():
    return "wlcm to fastapi"

@app.get("/products")
def get_products():
    return products


# path params = use when you know there will befixed dynamic values(min= 1, max = 2)
@app.get("/product/{product_id}")
def  get_one_product(product_id:int):

    # if product available with the id return product else not found

    for oneProduct in products:
        if oneProduct.get("id") == product_id:
            return oneProduct

    return {
        "error" : "Product not found for this id!"
    }

# query params = use when there will be n params 
@app.get("/greet")
def greet_user(request: Request):
    query_params= dict(request.query_params)
    print(query_params)
    return {
        "greet": f"Hello {query_params.get("name")},your age is {query_params.get("age")} "

    }