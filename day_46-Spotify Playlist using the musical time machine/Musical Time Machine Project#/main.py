import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
SPOTIPY_CLIENT_ID = "340238daf8ea4117b2b3875c221afb1e"
SPOTIPY_CLIENT_SECRET  = "aaa6f76b352544ed85c1e3771f883eed"
SPOTIPY_REDIRECT_URI = "http://example.com"

user_date_input = input("What date would you like to go back in time?format = 2010-07-24\n")
URL = f"https://www.billboard.com/charts/hot-100/{user_date_input}/"
year = user_date_input.split("-")[0]
#Web scrapping song from 100 top song.
response = requests.get(url=URL)
soup = BeautifulSoup(markup=response.text,features="html.parser")
song_name_list = soup.select(selector="li ul li h3")
# author_name_list = soup.select(selector="ul li ul li span")
author_name_list = soup.find_all("span",class_="a-no-trucate")
song_lists = []

#li ul li ul

#Adding name and author to lists
for index in range(len(song_name_list)):
    song_lists.append({
        "title":str(song_name_list[index].getText()).replace("\n","").replace("\t",""),
        "author":str(author_name_list[index].getText()).replace("\n","").replace("\t","")
                       })


scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"))

# result  = sp.search(q="track: Love the way you lie  year: 2010 ",type="track")
# print(result["tracks"]["items"][0]["uri"])

uri_list =[]
#find song and add uri to list, choose the first option.
for song in song_lists:
    try:
        result = sp.search(q=f"track: {song['title']}  year: {year} ",type="track")
        uri_list.append(result["tracks"]["items"][0]["uri"])
    except :
        print("Song not found")

#Create and upload music to playlist and print out the link to the playlist
user_id = sp.current_user()["id"]
playlist_name = f"{user_date_input} Billboard 100"
res = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=f"This playlist will take you back to {playlist_name} make you remember all the precious memory.")
sp.playlist_add_items(playlist_id=res["id"],items=uri_list)
print(f'Here is a link to your time machine: {res["external_urls"]["spotify"]}')