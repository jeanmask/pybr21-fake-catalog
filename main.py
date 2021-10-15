import json
import os
from pathlib import Path

from fastapi import FastAPI

DATA_DIR = Path(os.path.dirname(__file__)) / "data"

app = FastAPI()


def read_data(file_):
    return json.load(open(file_))


@app.get("/")
async def catalog_list():
    files = DATA_DIR.glob("*.json")
    return [read_data(f_) for f_ in files]


@app.get("/{code}")
async def catalog_retrieve(code):
    ...
