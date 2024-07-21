# Atlys Backend Assignment

Presenting you, the AtlysScraper in all it's glory! It's a fun tool which scrapes product data from a dental ecomm website and stores it in an in-memory DB.

## Setup
1. Run `pip install -r requirements.txt` to download all dependencies
2. Run `fastapi dev main.py` to run the FastAPI server
3. Hit `http://127.0.0.1:8000/docs` in the browser to view the OpenAPI docs
4. Input `qxdpbyt49@12` as static token for auth
5. Give the number of pages you want to scrape in the request body. Hit the API now
6. You will see a file called `db.json` created in the project which acts as the in-memory db (Pysondb). It has all the products which have been scraped. These products will only get updated if the prices change
7. All the images get downloaded in the `images` directory of the project

## Design decisions
1. A retry mechanism (3 times) has been provided with wait time of 2s between each
2. After the scraping is done, the number of products in DB is output through a notification service (`Strategy design pattern`)
3. This project can support a variety of databases with minimal code change due to the use of `repository design pattern`
4. `ThreadExecutorPool` has been used for multi-threading to boost the scraping speed 
5. Abstractions and OOPs principles have been followed wherever possible to make the codebase modular and extensible
6. Type validations have been done through `pydantic` library

## Screenshots

![Pic 1](https://github.com/user-attachments/assets/cb27f23e-9f21-42b7-b1d0-edf30eaf4600)

![Pic 2](https://github.com/user-attachments/assets/20256f0e-bd72-4065-a0e0-c7217f2b83fe)

![Pic 3](https://github.com/user-attachments/assets/600aad16-08f3-4f22-9b15-625c1f14db48)

## PS: Please delete the `db.json` file and `images` folder manually if you restart the server
