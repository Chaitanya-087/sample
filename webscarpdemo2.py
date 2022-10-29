import requests
from bs4 import BeautifulSoup

html_text = requests.get("https://en.wikipedia.org/wiki/Robot").text
soup = BeautifulSoup(html_text,'lxml')
types = soup.find_all('h3')
print("******TYPES OF ROBOTS******")
for type in  types:
    if type.text.endswith("robots") and len(type.span.text)!=0:
        print(type.span.text)