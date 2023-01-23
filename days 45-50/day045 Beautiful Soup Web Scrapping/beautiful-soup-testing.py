from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")

print(soup.title.string)
print(soup.a)

links = [anchor.get("href") for anchor in soup.find_all(name="a")]
print(links)

heading = soup.find(name="h1", id="name")
print(heading)

company_url = soup.select_one(selector="p a")
print(company_url.get("href"))

headings = soup.select(".heading")
print(headings)
