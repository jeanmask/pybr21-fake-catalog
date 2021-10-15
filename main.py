import json
import os
from pathlib import Path
from random import random

from fastapi import FastAPI
from fastapi.responses import JSONResponse

DATA_DIR = Path(os.path.dirname(__file__)) / "data"
FAIL_RATE = int(os.getenv("FAIL_RATE", 0))


app = FastAPI()


@app.middleware("http")
async def controlled_fail_middleware(request, call_next):
    if FAIL_RATE / 100 > random():
        return JSONResponse(status_code=500)
    return await call_next(request)


def read_data(file_):
    return json.load(open(file_))


@app.get("/")
async def catalog_list():
    files = DATA_DIR.glob("*.json")
    return [read_data(f_) for f_ in files]


@app.get("/{code}")
async def catalog_retrieve(code):
    return read_data(DATA_DIR / f"{code}.json")
