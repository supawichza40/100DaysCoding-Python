import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


# Write your code below this line 👇

response = requests.get(url=URL)
soup = BeautifulSoup(markup=response.text,features="html.parser")
data = soup.find(class_="article-title-description__text")
movie_list = data.find_all_next(class_="title")
movie_list.reverse()

with open("movies100ToWatch.txt","a",encoding="UTF-8") as writer:
    for movie in movie_list:
        writer.write(f"{movie.getText()}\n")


