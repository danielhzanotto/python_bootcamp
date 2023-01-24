import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPTF_ID = ""
SPTY_SECRET = ""
URI_redirect = "https://example.com"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPTF_ID,
                                               client_secret=SPTY_SECRET,
                                               redirect_uri=URI_redirect,
                                               scope="playlist-modify-private"))

results = sp.current_user()

user_id = results["id"]


date_travel = input("Which date do you want to travel to? (YYYY-MM-DD)")

billboard_url = "https://www.billboard.com/charts/hot-100/"

response = requests.get(billboard_url+date_travel)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")


titles_html = soup.select(
    ".lrv-u-width-100p .lrv-a-unstyle-list .o-chart-results-list__item #title-of-a-story")
titles = [title.string.strip() for title in titles_html]

authors_html = soup.select(
    ".lrv-u-width-100p .lrv-a-unstyle-list .o-chart-results-list__item .c-label")
authors = [author.string.strip()
           for author in authors_html if not author.string.strip().isnumeric() and author.string.strip() != "-"]


songs_uri = []
for i in range(0, len(authors) - 1):
    song = sp.search(titles[i] + authors[i], 1, 0, "track")
    songs_uri.append(song["tracks"]["items"][0]["uri"])
print(songs_uri)


playlist = sp.user_playlist_create(
    user=user_id, name=f"{date_travel} Billboard 100", public=False)
print(playlist)

playlist_id = playlist["id"]

sp.user_playlist_add_tracks(
    user=user_id, playlist_id=playlist_id, tracks=songs_uri)
