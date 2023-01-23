from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

article_tag = soup.find_all(name="span", class_="titleline")
article_anchors = [span.find(name="a") for span in article_tag]

article_links = [anchor.get("href") for anchor in article_anchors]
article_titles = [anchor.string for anchor in article_anchors]

article_points = [int(points.string.split(" ")[0])
                  for points in soup.find_all(class_="score")]
articles = [{"title": article_titles[i], "link": article_links[i], "points": article_points[i]}
            for i in range(29)]
print(articles)
