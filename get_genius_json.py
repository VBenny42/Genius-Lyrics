import token_my
from lyricsgenius import Genius
# import wikipedia
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# print(token_my.genius_token)
genius = Genius(token_my.genius_token)

# artist = genius.search_artist('Kanye West')
# artist.save_lyrics()

# kanye = wikipedia.page("Kanye_West_albums_discography")
# print(kanye.sections)

def show_html(URL_input):
    html = Request(URL_input, headers={'User-Agent':'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25'})
    return(urlopen(html).read())

def get_albums():
    weeknd_wiki = BeautifulSoup(show_html("https://en.wikipedia.org/wiki/The_Weeknd_discography"),'html.parser')
    album_list = []
    all_albums = weeknd_wiki.find_all("th", {"scope":"row"})
    studio_albums = all_albums[5:10]
    # print(studio_albums)
    for album in studio_albums:
        # print(album.i.a.string)
        album_list.append(album.i.a.string)

    mixtapes = all_albums[12:15]
    for mixtape in mixtapes:
        # print(mixtape.i.a.string)
        album_list.append(mixtape.i.a.string)

    return album_list

all_albums = get_albums()
# print(get_songs(all_albums[0]).prettify())
# genius.excluded_terms = ["(Live)", "Skit"]
# genius.skip_non_songs = True

for album in all_albums:
    album_json = genius.search_album(name=album, artist="The Weeknd")
    album_json.save_lyrics()