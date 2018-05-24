# 1. In a folder, enter "shell:sendto" in address bar
# 2. There, create a .cmd-file with:
#		@echo off
#		cls
#		python C:\Your\File\uploadscript.py %1
# 3. Voila! You can right click and send to python script

import subscene, requests, zipfile, io, sys

# Fetch string between last \ and .
inputParameter = sys.argv[1]
placeOfLastBackslash = inputParameter.rfind("\\")
placeOfDot = inputParameter.rfind(".")

# Find subtitles for title
filmReq = inputParameter[placeOfLastBackslash+1:placeOfDot]
listOfAllEngSubtitles = []
film = subscene.search(filmReq)

# Fetch all english subtitles
for subtitle in film.subtitles:
	if subtitle.language == "English":
		listOfAllEngSubtitles.append(subtitle)

r = requests.get(listOfAllEngSubtitles[0].zipped_url)
z = zipfile.ZipFile(io.BytesIO(r.content))

# Save in folder in which script was called from
z.extractall(inputParameter[:placeOfLastBackslash+1])
