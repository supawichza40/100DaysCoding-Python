from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")

movie_dict = []

soup = BeautifulSoup(markup=response.text, features="html.parser")

all_titles = soup.find_all(name="a", class_="titlelink")
for title in all_titles:
    movie_dict.append(
        {
            "title": title.getText()
        }
    )
all_points = soup.find_all(class_="subtext")
counter =0
for point in all_points:
    print(point.getText())
    if "points" in point.getText() or "point" in point.getText():
        movie_dict[counter]["point"] = int(point.getText().split(" ")[0])
    else:
        movie_dict[counter]["point"] = 0
    counter+=1

movie_dict.sort(key=lambda e: e["point"],reverse=True)
print(movie_dict)

# from bs4 import BeautifulSoup
#
# with open("website.html",encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# all_anchor_tag = soup.find_all(name="a")
# print((all_anchor_tag))
# for anchor in all_anchor_tag:
#     print(anchor)
