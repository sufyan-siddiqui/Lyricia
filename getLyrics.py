import lyricsgenius
from re import search

genius = lyricsgenius.Genius("o8qt7EBCuFPzv7uohBxtA3IHfdwtPyltGSwlPPKAqTmidVkUjABzxY7lnLOeegS-")
genius.verbose = False
genius.excluded_terms = ["(Remix)", "(Live)"] 
def searchFor(input):
	#input = input("Enter the query: ")
	if "-" not in input:
		print("Please use format Artist-Song")
		return
	artistName = input[:input.index('-')]
	artistName = artistName.strip()
	print(artistName)
	songName = input[input.index('-')+1:].strip()
	print(songName)
	artist = genius.search_artist(artistName, max_songs=None, sort="title", get_full_info=False, allow_name_change=False)
	##print(artist.name)
	print(artist.songs)


	if(artist is not None):
		exists = False
		for pair in artist.songs:
			pairSong = pair.title.strip()
			pairSong = pairSong.lower()
			if search(songName, pairSong):
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

