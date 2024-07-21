import os
from typing import Dict, List
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from bs4 import BeautifulSoup

from core.config import RETRIES, WAIT_TIME


def fetch_page(url: str):
    retries = RETRIES
    wait_time = WAIT_TIME
    for attempt in range(retries):
        try:
            response = requests.get(url)
            if 500 <= response.status_code < 600:
                raise Exception(f"Server error: {response.status_code}")
            return response
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(wait_time)
            else:
                raise e


def get_product_details(item) -> Dict:
    title = ""
    price = 0
    img_path = ""
    # Get price
    price_span = item.find('span', class_='woocommerce-Price-amount amount')
    if price_span:
        price = price_span.text
    # Get  title and thumbnail
    img_element = item.find('img')
    if img_element and 'data-lazy-src' in img_element.attrs:
        title = img_element['title'][:-20]
        img_url = img_element['data-lazy-src']
        response = requests.get(img_url)
        # Download image
        if response.status_code == 200:
            os.makedirs('images', exist_ok=True)
            img_path = os.path.join('images', os.path.basename(img_url))
            with open(img_path, 'wb') as file:
                file.write(response.content)
        else:
            print(f"Failed to download image: {response.status_code}")
    
    return {"product_title": title, "product_price": price, "path_to_image": img_path}


def scrape_products_page(url: str) -> List[Dict]:
    products = []
    ul_list = []
    try:
        response = fetch_page(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find(id='mf-shop-content')
        if div:
            ul = div.find('ul', class_='products columns-4')
            if ul:
                ul_list = ul.find_all('li')

        with ThreadPoolExecutor() as executor:
            products = list(executor.map(get_product_details, ul_list))

    except Exception as e:
        print(f"Failed to fetch page {url}: {e}")
    return products


def scrape_products(url: str, page_limit: int) -> List[Dict]:
    try:
        products = []
        with ThreadPoolExecutor() as executor:
            future_to_url = {executor.submit(scrape_products_page, f"{url}/page/{page}/"): page for page in range(1, page_limit + 1)}
            for future in as_completed(future_to_url):
                page_products = future.result()
                products.extend(page_products)
    except Exception as e:
        print(f"Error encountered: {e}")
    return products
