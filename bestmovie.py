import requests
from bs4 import BeautifulSoup

URL = 'https://www.empireonline.com/movies/features/best-movies-2/'
CLASS = 'listicleItem_listicle-item__title__hW_Kn'
response = requests.get(url=URL)
# print(response.status_code)
website_html = response.text


soup = BeautifulSoup(website_html, 'html.parser')
# print(soup.prettify)
all_movie = soup.find_all(name='h3', class_= CLASS)

movie_title = [movie.getText() for movie in all_movie]

# print(movie_title)
print(type(movie_title))
movies = movie_title[::-1]

with open ('BestMovie.txt','w') as file:
    for movie in movies:
        file.write(f'{movie} \n')

