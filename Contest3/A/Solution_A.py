team = int(input())
playlist = {}
for i in range(team):
    _ = int(input())
    songs = input().split()
    for song in songs:
        if song in playlist:
            playlist[song].append(i)
        else:
            playlist[song] = [i]

general_playlist = []
for song, likes in playlist.items():
    if len(likes) == team:
        general_playlist.append(song)

print(len(general_playlist))
print(*sorted(general_playlist), sep=' ')
