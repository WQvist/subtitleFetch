import subscene, requests, zipfile, io
listOfAllEngSubtitles = []
filmReq = input("Enter title: ")
film = subscene.search(filmReq)

# Fetch all english subtitles
for subtitle in film.subtitles:
	if subtitle.language == "English":
		listOfAllEngSubtitles.append(subtitle)

# Print all to choose
count = 1		
for subtitle in listOfAllEngSubtitles:
	print(count, subtitle.title)
	count+=1

indexOfDownload = input("Enter number to download: ")

r = requests.get(listOfAllEngSubtitles[int(indexOfDownload)-1].zipped_url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall("F:/")
