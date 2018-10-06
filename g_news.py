import re
import urllib
import urllib.request
import requests
from bs4 import BeautifulSoup as bs
from lev import LevenshteinSimilarity

class Get:
	def __init__(self):
		self.url = "https://news.google.com/?hl=ja&gl=JP&ceid=JP:ja"
		self.lev = LevenshteinSimilarity()
		self.response = requests.get(self.url)
		self.soup = bs(self.response.text, "lxml")

	def info(self, e):
		print("Title : {}".format(e.getText()))
		href = e.get("href")
		e_url = urllib.parse.urljoin(self.url,href)
		print("URL : {}\n".format(e_url))


	def get(self):
		elems = self.soup.find_all("a", class_="ipQwMb Q7tWef")
		i = 0
		for e in elems:
			if i==0:
				self.info(e)
			if i<len(elems)-1:
				if self.lev(elems[i].getText(),elems[i+1].getText()) < 0.018:
					self.info(e)		
			i+=1


if __name__ == '__main__':
	news = Get()
	news.get()




