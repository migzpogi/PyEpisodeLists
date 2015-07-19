watchlist="F:\Python Episodes\showlist.txt"
latestepisodes="F:\Python Episodes\latestpisodes.html"
maxepis=3

import requests
import bs4
import os

f = open(watchlist, 'r')
shows = f.readlines()
numofshows = len(shows)
f.close()

try:
	os.remove(latestepisodes)
except OSError:
	pass

x=0
while x<numofshows:
	response = requests.get(shows[x])
	soup = bs4.BeautifulSoup(response.text)

	titles = soup.find_all('td', class_='tlistname');

	for title in titles[0:maxepis]:

		showtitle = title.string
		showurl = title.a['href']
		file = open(latestepisodes, "a")
		file.write("<html><body>")
		file.write("<a href='")
		file.write(showurl)
		file.write("'>")
		file.write(showtitle)
		file.write("</a>")
		file.write("<br>")
		file.write("</body></html>")
		file.close()

	x += 1

print "\nDONE\n\n"