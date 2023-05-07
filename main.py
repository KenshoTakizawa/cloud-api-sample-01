from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"mess1ge": "Hello World"}