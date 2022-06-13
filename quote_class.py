import random
import requests
from bs4 import BeautifulSoup

class Quote:
    def __init__(self):
        self.url = "https://lpcryptogram.github.io/"
        self.html_file = self.scrape_website()
        self.quote_of_the_day = self.get_quote_of_the_day()

    def scrape_website(self):
        response = requests.get(self.url)
        html_file = BeautifulSoup(response.text, "html.parser")
        return html_file

    def get_quote_of_the_day(self):
        q_imgs = self.html_file.find_all("img", class_="quote-image")
        quote_image_of_the_day = random.choices(q_imgs, k=1)
        quote = quote_image_of_the_day[0]["alt"]
        return quote
