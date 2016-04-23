from __future__ import unicode_literals

from django.db import models

typeChoices = ( ('Myth','Myth'),('Fact','Fact'),('Story','Story'), )

# Create your models here.
class StoryAboutMoon(models.Model):
    text = models.CharField(max_length = 1000,blank=True,null=True)
    type = models.CharField(max_length = 10,choices = typeChoices,blank=True,null=True)
    image = models.ImageField(blank=True,null=True)

class ApolloImages(models.Model):
    image = models.ImageField(blank=True,null=True)
    description = models.CharField(max_length=1000)
