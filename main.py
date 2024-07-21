from fastapi import FastAPI
from api.scraper import scrape_router

app = FastAPI()

app.include_router(scrape_router, prefix="/scrape", tags=["scrape"])


@app.get("/")
def read_root():
    return {"message": "Welcome to Atlys backend challenge!"}
