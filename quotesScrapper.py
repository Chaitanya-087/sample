from bs4 import BeautifulSoup
import requests
import pandas as pd

BASE_URL = 'https://www.goodreads.com/quotes'
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

def getSoup(url):
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content,'html.parser')
    print(response.status_code)
    return soup.body


def getQuotes(page):
    soup = getSoup(BASE_URL + f'?pages={page}')
    quotes = [quote.text.strip().replace('\n','').split('    ―      ') for quote in soup.find_all('div',class_="quoteText")]
    return quotes

quotes = []
for i in range(20):
    quotes.extend(getQuotes(i+1))



quoteList = [quote[0] for quote in quotes]
authorList = [quote[1] for quote in quotes]


data = {
    'quote':quoteList,
    'author':authorList
}

df = pd.DataFrame(data)

df.to_json('quotes.json',orient='records')