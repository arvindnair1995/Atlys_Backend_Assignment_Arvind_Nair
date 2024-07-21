from typing import Dict, List

from fastapi import Depends

from repository.pyson_db import PysondbRepository
from utils.scraper import scrape_products


class ScraperService:
    def __init__(self, repository: PysondbRepository = Depends(PysondbRepository)):
        self.repository = repository

    def scrape_and_store(self, url: str, page_limit: int) -> List[Dict]:
        products = scrape_products(url, page_limit)
        for product in products:
            if product['product_title'] and self.repository.get_product_price(product['product_title']) != product['product_price']:
                self.repository.add_product(product)
        print(str(self.repository.get_products_size()) + " products were scraped in this DB session")
        return products
