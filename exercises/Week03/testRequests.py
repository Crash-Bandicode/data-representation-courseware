import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.git-tower.com/learn/git/ebook/en/command-line/basics/starting-with-an-unversioned-project#start")
print (page)
print ("------------")
print (page.content)
soup1 = BeautifulSoup(page.content)
print (soup1.prettify())