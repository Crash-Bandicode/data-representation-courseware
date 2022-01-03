import requests
import csv
from bs4 import BeautifulSoup
url = "https://www.property.ie/property-for-sale/cork/"
page = requests.get(url)

#print(page)

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

listings = soup.findAll("div", class_="search_result")
#print(listings[0])
for listing in listings:
    priceDiv = listing.find("div", class_="sresult_description").find("h3").text
    #addressDiv = listing.find("div", class_="sresult_address").find("<a>").text
    print(priceDiv)
    print("-------------")
