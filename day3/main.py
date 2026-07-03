from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running successfully"}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {
        "message": f"User with ID {user_id} retrieved successfully",
        "user_id" : user_id
    }


@app.get("/products/{product_id}")
def get_products(product_id:int):
    return {
        "message": f"Product with ID {product_id} retrieved successfully",
        "product_id" : product_id
    }

@app.get("/search")
def search(category: str, brand:str):
    return {
        "message": f"Search results for category '{category}' and brand '{brand}'",
        "category" : category,
        "brand" : brand
    }


@app.get("/students")
def get_students(name: str, age: int):
    return {
        "message": "Student details received",
        "name": name,
        "age": age
    }