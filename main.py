from fastapi import FastAPI, Request
from data import products
from dtos import ProductDTO
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


@app.post("/create_product")
def create_product(product_data: ProductDTO):
    product_data = product_data.model_dump()
    products.append(product_data)
    return products


@app.put("/update_product/{product_id}")
def update_product(product_data: ProductDTO, product_id:int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            products[index] = product_data.model_dump()
            return {"status": "product updated successfully!", "product":product_data}
        
    return {
         "error" : "Product not found for this id!"
    }


    
@app.delete("/delete_product/{product_id}")
def delete_product(product_id: int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            deleted_product = products.pop(index)
            return {"status": "successfully deleted!", "product": deleted_product}
    return {
 "error": "Product not found for this id!"
}        