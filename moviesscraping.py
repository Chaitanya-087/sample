import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/search/title/?groups=top_1000&sort=alpha,asc'
movies_content_list = []

def parse(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content,'html.parser')
  return soup.body

def get_movies_list_by_page(startvalue=1):
  content = parse(f'https://www.imdb.com/search/title/?groups=top_1000&sort=alpha,asc&start={startvalue}&ref_=adv_nxt')
  movies_name_by_page = content.find_all('div',class_='lister-item')
  return movies_name_by_page

def get_all():
    startvalue = 1
    while startvalue <= 1000:
        movies_content_list.extend(get_movies_list_by_page(startvalue))
        startvalue += 50

get_all()
movie_name_list = [movie.find('h3',class_='lister-item-header').find('a').text.strip() for movie in movies_content_list]
movie_poster_list = [movie.find('img')['src'].strip() for movie in movies_content_list]
movie_rating_list = [movie.find('strong').text.strip() if movie.find('strong') else "" for movie in movies_content_list]
movie_runtime_list = [movie.find('span',class_='runtime').text.strip() if movie.find('span',class_='runtime') else "" for movie in movies_content_list]
movie_certificate_list = [movie.find('span',class_='certificate').text.strip() if movie.find('span',class_='certificate') else "" for movie in movies_content_list]
movie_genre_list = [movie.find('span',class_='genre').text.strip() if movie.find('span',class_='genre') else "" for movie in movies_content_list]

data = {
    'key':[i for i in range(1,1001)],
    'name':movie_name_list,
    'poster':movie_poster_list,
    'rating':movie_rating_list,
    'runtime':movie_runtime_list,
    'certificate':movie_certificate_list,
    'genre':movie_genre_list
}

df = pd.DataFrame(data)

df.to_json('top1000movies.json',orient="records")