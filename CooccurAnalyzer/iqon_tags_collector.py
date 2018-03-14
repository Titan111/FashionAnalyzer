import urllib.request as url_req
from bs4 import BeautifulSoup

if __name__ == "__main__":
	root_href = "https://www.iqon.jp"
	list_href = root_href + "/sets/tag/%E3%83%A1%E3%83%B3%E3%82%BA/"

	for i in range(24,28):
		list_page = url_req.urlopen( list_href + "?page=" + str(i) )
		list_soup = BeautifulSoup( list_page , "lxml" )

		for box in list_soup.select("li.set-box"):
			sets_page = url_req.urlopen( root_href + box.a["href"] )
			sets_soup = BeautifulSoup( sets_page , "lxml" )
			for tag in sets_soup.select( "ul.set-tags a" ):
				print( tag.string[2:] ,end=" ")
			print("")


