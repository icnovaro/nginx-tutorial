from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
async def root():
    node = os.getenv("NODE")
    return {"message": f"Respondiendo desde el nodo: {node}"}
