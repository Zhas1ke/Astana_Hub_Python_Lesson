# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class KolesaItem(Item):
    # define the fields for your item here like:
	year = Field()
	price = Field()
	url = Field()
	ads_id = Field()
	link = Field()
	city = Field()
	manufacturer = Field()
	model = Field()
	body = Field()
	year = Field()
	age = Field()
	price = Field()
	volume = Field()
	engine_type = Field()
	transmission = Field()
	mileage = Field()
	helm = Field()
	color = Field()
	metallic = Field()
	photos = Field()
	drive = Field()
	description = Field()
	options = Field()