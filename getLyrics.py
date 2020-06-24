import lyricsgenius
import re
import os
import json

geniusToken = os.environ["GENIUS_TOKEN"]
genius = lyricsgenius.Genius(geniusToken)
genius.verbose = False
genius.excluded_terms = ["(Remix)", "(Live)"] 

def checkCache(artist):
	artist = "".join(artist.split())
#	songname = songname.strip()

	for root, dirs, files in os.walk(os.getcwd()):
		print(files)
		for file in files:
			if re.search(artist, file, re.IGNORECASE):
				return True, file
	return False, ""

def fromCache(songName, fileName):
	with open(fileName) as f:
		data = json.load(f)

	for song in data["songs"]:
		if re.search(songName, song["title"], re.IGNORECASE):
			return song["lyrics"]

def searchApi(artistName, songName):			
	print(artistName)
	
	print(songName)
	artist = genius.search_artist(artistName, max_songs=None, sort="title", get_full_info=False, allow_name_change=False)
	##print(artist.name)
	print(artist.songs)


	if(artist is not None):
		artist.save_lyrics()
		exists = False
		for pair in artist.songs:
			pairSong = pair.title.strip()
			pairSong = pairSong.lower()
			if re.search(songName, pairSong):
				exists = True
				break			
			else:
				continue
				
		if exists:
			song = genius.search_song(songName, artist.name)
			return song.lyrics
		else:
			return f"Song {songName} not Found By {artistName}"

	else:
		return "Artist not found"

def searchFor(input):
	#input = input("Enter the query: ")
	if "-" not in input:
		return "Please use format Artist-Song"
	
	artistName = input[:input.index('-')]
	artistName = artistName.strip()

	songName = input[input.index('-')+1:].strip()

	isCached, fileName = checkCache(artistName)

	if isCached:
		fromCache(songName, fileName)
	else: 
		searchApi(artistName, songName)


	
