# We can query the web using python libraries
import sys
# if requests library is not installed in your system, install it using pip
import requests
# there is a web site for itunes
url = 'https://itunes.apple.com/search'

# we need to pass some parameters to this url
term = 'Beatles'
media = 'music'
params = {'term':term, 'media':media}

response = requests.get(url, params=params).json()

results = response['results']

keys = results[0].keys()

def is_song(result):
    if result['kind'] == 'song':
        return True
    else:
        return False

songs = list(filter(is_song, results))

records = []
for song in songs:
    records.append({'trackName': song['trackName'], 'releaseDate':song['releaseDate']})
print(len(records))
print()
for record in records:
    print(record)


