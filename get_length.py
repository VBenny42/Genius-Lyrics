import json

file = open("The Weeknd Lyrics/Lyrics_Starboy_withList.json")

data = json.load(file)

print(len(data['tracks'])-1)
starboy = data['tracks'][0]

count = 0
total = 0
for lyric in starboy['song']['lyrics']:
    total += 1
    if "starboy" in lyric.lower():
        print(total, lyric)
        count += 1

print(count, total)