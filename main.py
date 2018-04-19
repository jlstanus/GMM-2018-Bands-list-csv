from lxml import html
import requests
import csv
import itertools

days = ('jeudi', 'vendredi','samedi','dimanche')
bandlist = []
for day in days :
	page = requests.get('https://www.graspop.be/fr/line-up/schedule/{}/?list=1'.format(day))
	tree = html.fromstring(page.content)
	bands = tree.xpath('//strong[@class="lineup__list__item__title"]/text()')
	bandlist.append(bands)
zipList = list(itertools.zip_longest(*bandlist))

with open('bands_v1.csv', 'w', newline='', encoding='utf-8') as csvfile:
	bandswriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	bandswriter.writerow(days)
	for row in zipList:
		bandswriter.writerow(row)
