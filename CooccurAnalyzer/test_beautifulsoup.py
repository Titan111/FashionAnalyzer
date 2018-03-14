import urllib.request as url_req
from bs4 import BeautifulSoup

html = url_req.urlopen("https://www.fashion-press.net/words/")

soup = BeautifulSoup(html,"lxml")

for tag in soup.find_all("a"):
	if "title" in tag.attrs:
		print(tag["title"])


