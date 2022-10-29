import requests
from bs4 import BeautifulSoup
import pandas as pd

def request(url):
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text,'lxml')
    return soup

soup = request('https://www.brainyquote.com/topics')
topics = soup.find_all('a',class_="topicIndexChicklet bq_on_link_cl")
q = {}
for topic in topics:
    name = topic.text.strip()

    if name.startswith('A'):
        l = []
        #print(f"Quotes on {name}".center(160))
        t = request(f'https://www.brainyquote.com/topics/{name.lower()}-quotes')
        quotes = t.find_all('div',style="display: flex;justify-content: space-between")
        for quote in quotes:
            l.append(quote.text.strip())
        q.update({name:l})
        # for index,quote in enumerate(quotes):
        #     print(f"{index+1}) {quote.text.strip()}")
        # print()
df = pd.DataFrame(q)
df.to_json()
