from typing import Dict, List

from fastapi import Depends

from notification.console import ConsoleNotification
from repository.pyson_db import PysondbRepository
from service.notification import NotificationService
from utils.scraper import scrape_products


class ScraperService:
    def __init__(self, repository: PysondbRepository = Depends(PysondbRepository)):
        self.repository = repository
        self.notification_service = NotificationService(ConsoleNotification())

    def scrape_and_store(self, url: str, page_limit: int) -> List[Dict]:
        products = scrape_products(url, page_limit)
        for product in products:
            if product['product_title'] and self.repository.get_product_price(product['product_title']) != product['product_price']:
                self.repository.add_product(product)
        self.notification_service.send_notification(str(self.repository.get_products_size()) + " products present in this DB session")
        return products
