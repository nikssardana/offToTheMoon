from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template.context_processors import csrf
from models import *
from tweepy import Stream,OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import os
import random
from django.contrib.auth.decorators import login_required
from django.contrib import auth

ckey = 'nwzgTPY9sYr0L70x61Z7Qzd5Z'
csecret = 'dRrOCyqH1Jp2j6fv0O9F4yPhvYXF0VmMx8ieyav30E275O13zs'
atoken = '63136441-BXcHjrKjvefkRbMYXho0ZFvShyGKLBbTUD03wizKB'
asecret = 'Ht3j7ChKwN0lb21hCo6HRMoUFIiOSzKmv1sjggQFT98vF'

@login_required
def index(request):
    return render_to_response('index.html',{})

@login_required
def whereAreYouMoon(request):
    dictValues = {}
    return render_to_response('whereAreYouMoon.html',dictValues)

@login_required
def moonStory(request):
    dictValues = {}
    dictValues = {}
    size = StoryAboutMoon.objects.all().count()
    #print "num of objects:",size
    rno = random.randint(0,size-1)
    randomStory = StoryAboutMoon.objects.all()[rno] #pick up a random story from the database
    dictValues['story'] = randomStory
    return render_to_response('moonStory.html',dictValues)

@login_required
def tripToApollo(request):
    dictValues = {}
    dictValues = {}
    size = ApolloImages.objects.all().count()
    #print "num of objects:",size
    rno = random.randint(0,size-1)
    randomStory = ApolloImages.objects.all()[rno] #pick up a random story from the database
    dictValues['apolloImage'] = randomStory
    return render_to_response('tripToApollo.html',dictValues)

@login_required
def doYouKnowMoon(request):
    dictValues = {}
    dictValues.update(csrf(request))
    questions = Question.objects.all()
    dictValues['questions'] = questions
    return render_to_response('doYouKnowMoon.html',dictValues)

@login_required
def checkAnswers(request):
    dictValues={}
    answers = []
    correctAnswers = []
    questions = Question.objects.all()
    score = 0
    for i in range(questions.count()):
        question = questions[i]
        ans = request.POST.get(str(i+1))
        answers.append(ans)
        correctAnswers.append(question.correctAns)
        if ans == question.correctAns:
            score+=1

    dictValues['score'] = score
    dictValues['list'] = zip(answers,correctAnswers)
    return render_to_response('checkAnswers.html',dictValues)

@login_required
def markMyTerritory(request):
    return render_to_response('markMyTerritory.html',{})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

def login(request):
    dictValues = {}
    dictValues.update(csrf(request))
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/')
    return render_to_response('login.html',dictValues)

#test views
class listener(StreamListener):
    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print status

def testView2(request):
    auth = OAuthHandler(ckey,csecret)
    auth.set_access_token(atoken,asecret)
    #twitterStream = Stream(auth,listener())
    #print twitterStream.filter(track=["car"])
    #text = twitterStream.filter(track=["car"])
    api = tweepy.API(auth)
    value = tweepy.Cursor(api.friends).items()
    value = value.next()
    print type(value)
    #value='hello'
    return HttpResponse(value)

def uploadImage(request):
    auth = OAuthHandler(ckey,csecret)
    auth.set_access_token(atoken,asecret)
    api = tweepy.API(auth)
    status = "testing"
    fn = os.path.abspath('/home/niks/Desktop/download.jpg')
    api.update_with_media(fn,status)
    return HttpResponse('Done')

def authorizeAndShowFriends(request):
    auth = OAuthHandler(ckey,csecret)
    callback_url = 'http://127.0.0.1:8000/test'
    auth = tweepy.OAuthHandler(ckey, csecret, callback_url)
    if not request.GET.get('oauth_token'):
        return HttpResponseRedirect(auth.get_authorization_url())
    request.session['request_token'] = request.GET.get('oauth_token')
    print "auth.request_token:",request.GET.get('oauth_token')

    #auth.set_access_token(atoken,asecret)
    auth.access_token = request.session.get('request_token')
    api = tweepy.API(auth)
    friends = api.friends()
    print "Friends:",friends
    return HttpResponse(friends)
