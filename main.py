from fastapi import Depends, FastAPI

from api.scraper import scrape_router
from auth.auth import verify_token

app = FastAPI()

app.include_router(scrape_router, prefix="/scrape", tags=["scrape"])


@app.get("/", dependencies=[Depends(verify_token)])
def read_root():
    return {"message": "Welcome to Atlys backend challenge!"}
