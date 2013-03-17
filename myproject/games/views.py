from django.template import RequestContext, Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_list_or_404, render
from django.views.generic import list_detail
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.core import serializers
from django.forms import ModelForm
from games.models import Game
from games.models import GameForm
from django.core.exceptions import ObjectDoesNotExist

def addGame(request):

	template = loader.get_template('add_game.html')
	dict = {'title_name': "Add Game", 'company': 'Block4Block'}

	if (request.method == 'POST'):
		game = GameForm(request.POST)
		if (game.is_valid()):
			if (game.cleaned_data['visits'] == 0):
				try:
					g = Game.objects.get(embed_src = game.cleaned_data['embed_src'])
					dict['message'] = g.name + ' Already Exists, Try Again'
				except ObjectDoesNotExist:
					game.save()
					dict['message'] = game.cleaned_data['name'] + ' submitted! You Can Add Another Game!'
			else:
				dict['message'] = 'Password Is Incorrect, Try Again'
		else:
			dict['message'] = 'Information Could Not Be Stored, Try Again'
	else:
		dict['message'] = 'Add New Game Here'
		game = GameForm()
		dict['form'] = game

	c = RequestContext(request, dict)
	return HttpResponse(template.render(c))

def game(request, game_id):
	template = loader.get_template('game.html')
	g = Game.objects.get(id = game_id)
	dict = {'title_name': g.name, 'company': 'Block4Block', 'Game': g}	
	c = RequestContext(request, dict)
	return HttpResponse(template.render(c))