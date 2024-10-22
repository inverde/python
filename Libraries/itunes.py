# We can query the web using python libraries
import sys
# if requests library is not installed in your system, install it using pip
import requests
# there is a web site for itunes
url = 'https://itunes.apple.com/search'

def search_tunes(term):
    params = {'term':term, 'media':'music'}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()['results']
    else:
        raise exception('Application Error: ' + str(response.status_code))


# we need to pass some parameters to this url
term = 'Beatles'
media = 'music'
params = {'term':term, 'media':media}



def is_song(result):
    if result['kind'] == 'song':
        return True
    else:
        return False

def get_songs(term):
    results = search_tunes(term)
    songs = list(filter(is_song, results))

    records = []
    for song in songs:
        records.append({'song': song['trackName'], 'album':song['collectionName'], 'premiere':song['releaseDate']})
    return records

def printList(listname, title='songs records'):
    print(f"This list has {len(listname)} {title}: \n\n")
    for rec in listname:
        print(f"Canción: {rec['song']}")
        print(f"Album: {rec['album']}")
        print(f"Estreno:: {rec['premiere']}", '\n')

def main():
    response = requests.get(url, params=params).json()
    results = response['results']
    keys = results[0].keys()
    print(keys)
    print()
    print(results)

if __name__ == "__main__":
    main()




