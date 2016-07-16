import requests
from bs4 import BeautifulSoup
import re


site = 'https://semo.craigslist.org/search/sss'

class Scraper(object):

	def __init__(self, site):
		self.site = site

	def soup_it(self):

		# Returns the BeautifulSoup object of the website we store in the variable /site/

		session = requests.Session()
		mainpage = session.get(self.site)
		requests_text_mainpage = mainpage.text
		return BeautifulSoup(requests_text_mainpage, "html5lib")

	def get_items(self):
		self.soup = self.soup_it()

		titles = self.get_titles()

		prices = self.get_price()

		return zip(titles,prices)

	def get_titles(self):

		# Finds the title of items being sold.

		hdrlnk_class = self.soup.find_all(class_='hdrlnk')

		titles = []

		try:
			for title_text in hdrlnk_class:
				title = str(title_text.get_text())
				titles.append(title)
		except UnicodeEncodeError:
			print("This one is unicode")
			pass

		return titles


	def get_price(self):

		# Finds the price of the items.

		price_class = self.soup.find_all('span', class_='price')

		prices = []

		try:
			for price_text in price_class[::2]:
				price1 = float(price_text.get_text().strip('$'))
				prices.append(price1)

		except UnicodeEncodeError:
			print("This one is unicode")
			pass

		return prices

scraper = Scraper(site='https://semo.craigslist.org/search/sss')

print(scraper.get_items())
