import requests
from bs4 import BeautifulSoup

response = requests.get(url='https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')
titles = soup.find_all(name='h3', class_='title')
movies = [title.string for title in titles]
movie_list = movies[::-1]

with open('movies.txt', mode='a') as file:
    for movie in movie_list:
        file.write(f'{movie}\n')



