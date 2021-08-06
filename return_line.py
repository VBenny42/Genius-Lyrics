import json
from random import randint

all_albums = {
    0:"Lyrics_AfterHours_withList.json",
    1:"Lyrics_BeautyBehindtheMadness_withList.json",
    2:"Lyrics_EchoesofSilence_withList.json",
    3:"Lyrics_HouseofBalloons_withList.json",
    4:"Lyrics_KissLand_withList.json",
    5:"Lyrics_Starboy_withList.json",
    6:"Lyrics_Thursday_withList.json",
    7:"Lyrics_Trilogy_withList.json"
}

albumnumber = randint(0, len(all_albums)-1)
file = open(all_albums[albumnumber])
# file = open("The\ Weeknd\ Lyrics/.{}".format(all_albums[albumnumber]))

data = json.load(file)

songnumber = randint(0, len(data['tracks'])-1)
lyricnumber = randint(0, len(data['tracks'][songnumber]['song']['lyrics'])-1 )
print(albumnumber, songnumber, lyricnumber)
print(data['tracks'][songnumber]['song']['lyrics'][lyricnumber])
print(data['cover_art_url'])