from fastapi import FastAPI
import os


app = FastAPI()


@app.get("/")
async def catalog_list():
    ...


@app.get("/{code}")
async def catalog_retrieve(code):
    ...
