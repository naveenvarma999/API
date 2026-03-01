from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def Home():
    return {"meggage": "My first api app is running"}