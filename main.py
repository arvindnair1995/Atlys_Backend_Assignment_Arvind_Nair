from fastapi import Depends, FastAPI

from api.scraper import scrape_router
from auth.auth import verify_token

app = FastAPI()

app.include_router(scrape_router, prefix="/scrape", tags=["scrape"])

