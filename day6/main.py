from fastapi import FastAPI
from pydantic import Field, BaseModel

app = FastAPI()

class userCreate(BaseModel):
    name : str = Field(min_length= 2, max_length = 100)
    email : str
    password : str

class userResponse(BaseModel):
    name : str
    email : str


@app.get("/")
def home(): 
    return {"message": "API is running successfully with validation"}   


@app.post("/users", response_model = userResponse)
def create_user(user: userCreate):
    return user 