from django.template import RequestContext, Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_list_or_404, render
from django.views.generic import list_detail
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.core import serializers
from django.forms import ModelForm
from games.models import Game
from django.views.generic.simple import direct_to_template
from django.core.paginator import Paginator, InvalidPage
from myproject.forms import searchForm

NUMELEMENTS = 12
SEARCHELEMENTS = 30

def home(request):
	template = loader.get_template('home.html')
	gamesList = Game.objects.all().order_by('-popularity')
	newList = getNElementsInList(NUMELEMENTS ,gamesList, 0)
	dict = {'title_name': "home", 'company': 'Block4Block', 'gamesList': newList, 'homeMsg': "Here are our most popular games!"}
	c = RequestContext(request, dict)
	return HttpResponse(template.render(c))

def mochi(request):
	template = loader.get_template('mochi.html')
	dict = {}
	c = RequestContext(request, dict)
	return HttpResponse(template.render(c))

def search(request):

	numFound = ""

	if (request.method == 'POST'):
		s = searchForm(request.POST)

		if (s.is_valid()):
			category = s.cleaned_data['category']
			c = replaceUnderscoreWithSpace(category)

			if (c == "All"):
				gList = Game.objects.all()
			else:
				gList = Game.objects.filter(category = c)

			numFound = str(len(gList)) + " " + c + " games found. Scroll to bottom to view all games."
			gamesList = gList.order_by('-popularity')
			paginator = Paginator(gamesList, SEARCHELEMENTS)
    		page_obj = paginator.page(1)

		context = {
			'title_name': "search", 
			'company': 'Block4Block',
			"gamesList": page_obj.object_list,
			"page": page_obj,
			"category": category,
			"NoGamesFound": "",
			"numFound": numFound
		}

		if (len(page_obj.object_list) == 0):
			context["NoGamesFound"] = "Your search returned zero games, please try again!"

	else:
		context = {
			'title_name': "search", 
			'company': 'Block4Block',
			"gamesList": "",
			"NoGamesFound": "Search for games by selecting a category!",
			"numFound": numFound
		}

	template = 'search.html'
	return direct_to_template(request, template, context)

def search_scroll(request, category):
	c = replaceUnderscoreWithSpace(category)

	if (c == "All"):
		gList = Game.objects.all()
	else:
		gList = Game.objects.filter(category = c)

	gamesList = gList.order_by('-popularity')
	paginator = Paginator(gamesList, SEARCHELEMENTS)

	if request.method == 'GET':
		if request.is_ajax():
			if request.GET.get('page_number'):
				# Paginate based on the page number in the GET request
				page_number = request.GET.get('page_number');
				try:
					page_objects = paginator.page(page_number).object_list
				except InvalidPage:
					return HttpResponseBadRequest(mimetype="json")
				# Serialize the paginated objects
				resp = serializers.serialize('json', page_objects)	
				return HttpResponse(resp, mimetype='application/json')
	else:
		page_obj = paginator.page(1).object_list

	context = {
		'title_name': "search", 
		'company': 'Block4Block',
		"gamesList": page_obj.gamesList,
		"page": page_obj,
		"category": category
		}
	c = RequestContext(request, dict)
	return direct_to_template(request, template, context)

###########################################################################################################

# assume sorted list, page number starts with 0
def getNElementsInList(numElements, gamesList, page):

	returnList = []
	startindex = page*numElements

	while (startindex < ((page + 1) * numElements) and startindex < len(gamesList)):
		returnList.append(gamesList[startindex])
		startindex = startindex + 1

	return returnList

# replace underscores with spaces
def replaceUnderscoreWithSpace(word):
	
	newWord = ""

	for letter in word:
		if (letter == '_'):
			newWord = newWord + " "
		else:
			newWord = newWord + letter

	return newWord
