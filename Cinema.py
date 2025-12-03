from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from os import getenv
import json


load_dotenv()



def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.kinoaero.cz/")
        page.wait_for_selector(".program__movie-name")

        film_name = page.locator(".program__movie-name").first.inner_text().strip()
        print("Film z Aero:", film_name)

        
        page.goto("https://www.csfd.cz/")
        page.wait_for_selector("input.tt-input")

       
        page.fill("input.tt-input", film_name)

        
        page.click(".btn-search")

        page.click('.film-title-name')

        
        rating = page.locator(".film-rating-average").first.inner_text().strip()

        print("Rating na CSFD:", rating)
        
        data = {
            "film": film_name,
            "rating": rating
        }

        with open("movies.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print("Uloženo do movies.json!")
        

        input("Hotovo, Enter pro ukončení...")
        browser.close()

if __name__ == "__main__":
    main()
