def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album

print(make_album('Sheila On 7', 'Kita'))
print(make_album('Hindia', 'Membasuh'))
print(make_album('Tulus', 'Monokrom', 10))