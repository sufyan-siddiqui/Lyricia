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
			lyrics = song["lyrics"]
			if lyrics is not None:
				return song["lyrics"]
			else:
				return "Sorry, but it appears I do not have the lyrics of this song"
		else:
			return "Hmm..it looks like I can't find the song \""+songName+"\"\nmaybe you didn't type the name correctly"

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
			return f"It appears that the Song \"{songName}\" by \"{artistName}\" does not exist in my database"

	else:
		return f"Are you sure you typed the artist's name right? I do not know anyone by the name \"{artistName}\""

def searchFor(input):
	#input = input("Enter the query: ")
	if "-" not in input:
		return "**Please make sure you separate the aritist's and song's name with a hyphen**\nExample: ArtistName-SongName"
	
	artistName = input[:input.index('-')]
	artistName = artistName.strip()

	songName = input[input.index('-')+1:].strip()

	isCached, fileName = checkCache(artistName)

	if isCached:
		response = fromCache(songName, fileName)
	else: 
		response = searchApi(artistName, songName)

	return response
	
