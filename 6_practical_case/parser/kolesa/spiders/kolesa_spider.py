from scrapy import Spider, Request
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
from kolesa.items import KolesaItem
import re
from datetime import date

class KolesaSpider(Spider):
	name = "kolesa"
	allowed_domains = ["kolesa.kz"]
	start_urls = ["https://kolesa.kz/cars/?auto-custom=2&auto-emergency=1&auto-car-order=1&page=1"]
	i = 0

	def parse(self, response):
		print (response.url)
		page = BeautifulSoup(response.text, 'lxml')
		links = page.select('div.result-block.col-sm-8 div.list-title a.list-link')
		links = ['https://kolesa.kz' + link.get('href') for link in links]
		for link in links:
			yield Request(link, callback=self.parse_item)

		next_link = 'https://kolesa.kz' + page.select('a.right-arrow.next_page')[0]['href'].strip()
		yield Request(next_link, callback=self.parse)

	def parse_item(self, response):
		url = response.url
		link = url
		ads_id = ''.join(re.findall('\d+', url))
		self.i += 1
		print (self.i, url)
		page = BeautifulSoup(response.text, 'lxml')

		features = page.select('dl.clearfix.dl-horizontal.description-params dt.value-title') 
		values = page.select('dl.clearfix.dl-horizontal.description-params dd.value.clearfix')

		features_strip = []
		values_strip = []

		for feature in features:
			feature_strip = feature.get_text().strip()
			if (feature_strip != ''):
				features_strip.append(feature_strip)

		for value in values:
			value_strip = value.get_text().strip()
			if (value_strip != ''):
				values_strip.append(value_strip)

		pairs = {}
		for i in range(0, len(features_strip)):
			pairs[features_strip[i]] = values_strip[i]

		city = pairs['Город']

		body = pairs['Кузов']
		s = pairs['Объем двигателя, л']
		engine_type = s[s.find("(") + 1 : s.find(")")]
		volume = float(s[:s.find("(")])

		transmission = pairs['Коробка передач']
		helm = pairs['Руль']
		try:
			color = pairs['Цвет'].split()[0]
			metallic = len(pairs['Цвет'].split()) - 1
		except:
			color = ''
			metallic = 0

		try:
			drive = pairs['Привод']
		except:
			drive = ''
		custom = pairs['Растаможен']
		try:
			mileage = int(''.join(re.findall('\d+', pairs['Пробег'])))
		except:
			mileage = None

		index = page.select('div.a-title__container')[0].get_text().split().index('года')

		year = int(page.select('div.a-title__container')[0].get_text().split()[index - 1])

		age = date.today().year - year
		
		price_string = page.select('span.a-price__text')[0].get_text().strip()[:-1]
		price = int(''.join(re.findall('\d+', price_string)))
		
		try:
			options = page.select('div.a-params')[0].get_text().strip()
		except:
			options = ''
		
		try:
			photos = len(page.select('ul.photo-list')[0])
		except:
			photos = 0

		try:
			description = page.select('div.description-text')[0].get_text().strip()
			description = ' '.join(description.split())
		except:
			description = ''

		manufacturer = page.select('h1.a-title__text span')[0].get_text().strip()
		model = page.select('h1.a-title__text span')[1].get_text().strip()

		main_options = {
			'ads_id': ads_id,
			'link': link,
			'city': city,
			'manufacturer': manufacturer,
			'model': model,
			'body': body,
			'year': year,
			'age': age,
			'price': price,
			'volume': volume,
			'engine_type': engine_type,
			'transmission': transmission,
			'mileage': mileage,
			'helm': helm,
			'color': color,
			'metallic': metallic,
			'photos': photos,
			'drive': drive,
			'description': description,
			'options': options
		}
		item = KolesaItem()
		for key, value in main_options.items():
			item[key] = value
		# item['url'] = url
		# item['year'] = year
		# item['price'] = price
		return item