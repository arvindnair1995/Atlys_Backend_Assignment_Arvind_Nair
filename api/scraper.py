from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field, HttpUrl
from auth.auth import verify_token
from core.config import URL
from service.scraper import ScraperService

scrape_router = APIRouter()

class ScrapeRequest(BaseModel):
    url: HttpUrl = Field(default=URL)
    page_limit: int = Field(default=1, gt=0, lt=120, description="Number of pages should be gretaer than 0 and less than 120")

@scrape_router.post("/", dependencies=[Depends(verify_token)])
async def scrape_data(request: ScrapeRequest, scraper_service: ScraperService = Depends()):
    try:
        if request.url != HttpUrl(URL):
           raise HTTPException(status_code=500, detail="URL cannot be changed")
        result = scraper_service.scrape_and_store(request.url, request.page_limit)
        return {"message": "Scraping completed successfully", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
