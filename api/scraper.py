from fastapi import APIRouter, HTTPException, Depends
from pydantic import HttpUrl

from auth.auth import verify_token
from core.config import URL
from schema.scraper import ScrapeRequest, ScrapeResponse
from service.scraper import ScraperService

scrape_router = APIRouter()

@scrape_router.post("/", dependencies=[Depends(verify_token)])
async def scrape_data(request: ScrapeRequest, scraper_service: ScraperService = Depends()) -> ScrapeResponse:
    try:
        if request.url != HttpUrl(URL):
           raise HTTPException(status_code=500, detail="URL cannot be changed")
        result = scraper_service.scrape_and_store(request.url, request.page_limit)
        return ScrapeResponse(message="Scraping completed successfully", data=result)
    except Exception as e:
        return ScrapeResponse(message="Scraping failed", data=str(e))
