from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

typeChoices = ( ('Myth','Myth'),('Fact','Fact'),('Story','Story'), )

# Create your models here.
class StoryAboutMoon(models.Model): #objects for moon story
    text = models.CharField(max_length = 1000,blank=True,null=True)
    type = models.CharField(max_length = 10,choices = typeChoices,blank=True,null=True)
    image = models.ImageField(blank=True,null=True)

class ApolloImages(models.Model): #objects for trip to apollo
    image = models.ImageField(blank=True,null=True)
    description = models.CharField(max_length=1000)

class Question(models.Model): #questions for quiz
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    correctAns = models.CharField(max_length=50)

class MyTent(models.Model): #list of items in the tent
    #Items required for survival will increase depending on the questions answered in quiz
    #and decrease after a specific time interval
    #A plant will convert O2 and H2 into water. Some water will be given to plant which will produce oxygen and the rest will be drunk by the player
    Oxygen = models.IntegerField(default=20)
    Hydrogen = models.IntegerField(default=10)
    Water = models.IntegerField(default=10)
    Poop = models.IntegerField(default=10)
    Fuel = models.IntegerField(default=0) #Will be required to run the hover
    CarbonDioxide = models.IntegerField(default=10) #Amount of CO2 will increase after specific time interval
    Food = models.IntegerField(default=10)
    Visited = models.BooleanField(default=False) #Check if this is the user's first visit or not
    User = models.ForeignKey(User) #User with whom the tent is associated
