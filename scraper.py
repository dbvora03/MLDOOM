import requests
from bs4 import BeautifulSoup
import os
import re

GENIUS_API_TOKEN = 'mTpFj3bH6sp0UH9vQsUNfyMuo8wbOnLK17Vtp_rgV96z1SoU7VyjbKcmt_fyFVap'

# Get artist object from Genius API
def request_artist_info(artist_name, page):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + GENIUS_API_TOKEN}
    search_url = base_url + '/search?per_page=10&page=' + str(page)
    data = {'q': artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response
# Get Genius.com song url's from artist object
def request_song_url(song_cap):
    page = 1
    songs = []
    artist_name = 'MF DOOM'
    while True:
        response = request_artist_info(artist_name, page)
        json = response.json()
        # Collect up to song_cap song objects from artist
        song_info = []
        for hit in json['response']['hits']:
            if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
                song_info.append(hit)
    
        # Collect song URL's from song objects
        for song in song_info:
            if (len(songs) < song_cap):
                url = song['result']['url']
                songs.append(url)
            
        if (len(songs) == song_cap):
            break
        else:
            page += 1
        
    print('Found {} songs by {}'.format(len(songs), artist_name))
    return songs
    
# DEMO
request_artist = request_song_url(70)

# Scrape lyrics from a Genius.com song URL
def scrape_song_lyrics(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = ''
    if html.find('div', class_='lyrics') is None:
        pass
    else:
        lyrics = html.find('div', class_='lyrics').get_text()
    #remove identifiers like chorus, verse, etc
    lyrics = re.sub(r'[\(\[].*?[\)\]]', '', lyrics)
    #remove empty lines
    lyrics = os.linesep.join([s for s in lyrics.splitlines() if s])         
    return lyrics
# DEMO

def write_lyrics_to_file():
    f = open('mfdoom.txt', 'wb')
    hi = 1
    for url in request_artist:
        print(hi)
        lyrics = scrape_song_lyrics(url)
        f.write(lyrics.encode("utf8"))
        hi += 1
    print("Done")


write_lyrics_to_file()