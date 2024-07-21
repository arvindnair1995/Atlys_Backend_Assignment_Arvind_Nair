from pydantic import BaseModel, Field, HttpUrl

from core.config import URL


class ScrapeRequest(BaseModel):
    url: HttpUrl = Field(default=URL, description="URL to be scraped")
    page_limit: int = Field(default=1, gt=0, lt=120, description="Number of pages should be gretaer than 0 and less than 120")


class ScrapeResponse(BaseModel):
    message: str = Field(..., description="A message about the scrape result.")
    data: str = Field(..., description="Number of products in DB.")