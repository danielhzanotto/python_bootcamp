import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

titles = [title.string for title in soup.find_all(name="h3", class_="title")]
titles.reverse()

with open("movies.txt", "w", encoding="utf-8") as f:
    for title in titles:
        f.write(title)
        f.write("\n")
