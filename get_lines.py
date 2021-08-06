import json
import sys
import pprint

file = open(sys.argv[1])

data = json.load(file)

to_be_kept = []
for track in data['tracks']:
    title = track['song']['title_with_featured']
    if 'skit' in title.lower() or 'booklet' in title.lower():
        continue
    track['song']['lyrics'] = track['song']['lyrics'].split("\n")[:-1]
    lyrics = []
    for lyric in track['song']['lyrics']:
        if "[" in lyric.lower() or "]" in lyric.lower() or lyric == "":
            continue
        lyrics.append(lyric)
    track['song']['lyrics'] = lyrics
    to_be_kept.append(track)
    # print(title)

# print(data['tracks'])

data['tracks'] = to_be_kept

# for track in data['tracks']:
#     title = track['song']['title_with_featured']
#     print(title)

# pprint.pprint(data)
f = open('{}_withList.json'.format(sys.argv[1].split(".", maxsplit=1)[0]), 'w',)
json.dump(data, f, indent=2)
