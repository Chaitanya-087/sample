from bs4 import BeautifulSoup
import requests
import pandas as pd

genre = []
links = []
title = []
date = []

base_url = 'https://www.themoviedb.org' 
def request(url):
  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
  html = requests.get(url,headers=headers) #https://www.themoviedb.org/movie?page=1
  contents = html.content
  soup = BeautifulSoup(contents,'lxml')
  return soup

for x in range(1,6):
  soup = request(f'https://www.themoviedb.org/movie?page={x}')
  h_tags = soup.select("h2 a")
  titles =[t.get_text() for t in h_tags]
  l = [base_url + link['href'] for link in h_tags]
  dates = soup.select("div.content p")
  d = [date.text for date in dates if date.text != 'Search' and date.text != 'Load More']
  date.extend(d)
  title.extend(titles)
  links.extend(l)

for link in links:
  soup = request(link)
  facts = soup.select("div.facts span.genres")
  for fact in facts:
    genre.append(fact.text.strip())


df = pd.DataFrame({'title':title,'release_date':date,'genre':genre,'link':links})
df.to_csv('movies.csv')