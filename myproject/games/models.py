from django.db import models
from django.forms import ModelForm

class Game(models.Model):

    # title of game
    name = models.CharField(max_length = 100)

    # link of image tile
    image = models.URLField()

    # category of game
    category = models.CharField(max_length = 100)

    # PG-13 or Everyone or Mature, ETC...
    content_rating = models.CharField(max_length = 50)

    # Description of Game
    description = models.TextField(max_length = 10000)

    # embedded code information from Mochi Media
    embed_src = models.CharField(max_length = 1000)
    embed_width = models.IntegerField()
    embed_height = models.IntegerField()

    # instructions and controls to play game
    instructions = models.TextField(max_length = 10000)
    controls_scheme = models.CharField(max_length = 5000)

    # number of times game page is visited
    visits = models.IntegerField()

    # What website
    site_type = models.CharField(max_length = 50)

    popularity = models.IntegerField()
    tags = models.CharField(max_length = 3000)
    categories = models.CharField(max_length = 1000)
    author = models.CharField(max_length = 50)
    updated = models.CharField(max_length = 100)

    donated = models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        return self.name

class GameForm(ModelForm):
    class Meta:
        model = Game

