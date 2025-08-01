from bs4 import BeautifulSoup
import requests
URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
h2_tags = soup.find_all("h2")
movies_titles = []
for h2 in h2_tags:
    strong_tag = h2.find("strong")
    if strong_tag:
        movies_titles.append(strong_tag.getText(strip=True))
movies = movies_titles[::-1]
with open("movies_to_watch.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")