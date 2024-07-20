from typing import Union
from fastapi import FastAPI
from strategy.db_strategy import PysonDBStrategy

app = FastAPI()

db_strategy = PysonDBStrategy()
db_strategy.setup()


@app.get("/")
def read_root():
    return {"message": "Welcome to Atlys backend challenge!"}
