import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/2010-07-24/"

response = requests.get(url=URL)
soup = BeautifulSoup(markup=response.text,features="html.parser")
song_name_list = soup.find_all(id="title-of-a-story")
for song in song_name_list:
    print(song)