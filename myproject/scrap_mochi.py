import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'myproject.settings')
from games.models import Game 
from django.core.exceptions import ObjectDoesNotExist
import re
import urllib
import httplib
import lxml
from lxml import html
import time, datetime
import json

def scrape_game():
	resp = open("download.json", 'r')
	data = resp.read()
	resp.close()
	parse_data(data)

def parse_data(data):
	page = json.loads(data)
	count = 1

	for child in page['games']:
		print "%d" %count
#		print '%d: %s' %(count,child['name'].title())
#		print 'Thumbnail_url: %s' %child['thumbnail_url']
#		print 'Rating: %s' %child['rating']
#		print 'Category: %s' %child['category']
#		print 'Description: %s' %child['description']
#		print 'Instructions: %s' %child['instructions']
#		print 'Control Scheme: %s' %(parse_controls(child['control_scheme']))
#		print 'Height: %s' %child['height']
#		print 'Width: %s' %child['width']
#		print 'SWF: %s' %child['swf_url']
#		print 'Site Type: mochimedia'
#		print 'Tags: %s' %child['tags']
#		print 'Popularity: %s' %child['popularity']
#		print 'Other Categories: %s' %child['categories']
#		print 'Author: %s ' %child['author']
#		print 'Last Updated: %s\n' %child['updated']

		try:
			g = Game.objects.get(embed_src = child['swf_url'])

			#check if last updated is the same as before, if not then update: for later

		except ObjectDoesNotExist:
			g = updateGame(child)
			g.save()

		count = count + 1

def updateGame(child):

	con = parse_controls(child['control_scheme'])
	inst = child['instructions']

	if (con == None):
		con = "None"

	if (inst == ""):
		inst = "None"

	return Game(name = child['name'].title(),
			image = child['thumbnail_url'],
			category = child['category'],
			content_rating = child['rating'],
			description = child['description'],
			embed_src = child['swf_url'],
			embed_width = int(child['width']),
			embed_height = int(child['height']),
			instructions = inst,
			controls_scheme = con,
			visits = 0,
			site_type = "mochimedia",
			popularity = int(child['popularity']),
			tags = "",#child["tags"],
			categories = child['categories'],
			author = child['author'],
			updated = child['updated'],
			donated = 0.00)

def parse_controls(controls):

	#group = re.findall('\w', controls)
	#sentence = ""
	#next = 2
	#print "Group: %s" %group
	return controls

if __name__ == '__main__':
	scrape_game()
