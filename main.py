from scraper import extract_company

import requests
from bs4 import BeautifulSoup


url = "https://www.indeed.com/q-data-analyst-$60,000-l-New-Jersey-jobs.html"

page = requests.get(url)
soup = BeautifulSoup(page.text,"html.parser")

companies = extract_company(soup)
print(companies)