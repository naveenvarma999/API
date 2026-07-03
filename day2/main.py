from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "API is running successfully"}

@app.get("/user")
def get_user():
    return {
        "name" : "Nallapu Naveen",
        "Role" : "ML Engineer",
        "mail" : "naveen@gmail.com"   }


@app.get("/products")
def get_products():
    return {
        "products": [
            {"id": 1, "name": "Laptop", "price": 50000},
            {"id": 2, "name": "Phone", "price": 25000},
            {"id": 3, "name": "Headphones", "price": 2000}
        ]
    }

@app.get("/about")
def about():
    return {
        "course": "API Practical Learning",
        "day": 2,
        "topic": "Multiple GET endpoints"
    }