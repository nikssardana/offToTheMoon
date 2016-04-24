"""OffToMoon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from NasaSpace import views

urlpatterns = [
    #actual urls
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),

    url(r'^whereAreYouMoon$', views.whereAreYouMoon),
    url(r'^moonStory$', views.moonStory),
    url(r'^tripToApollo$', views.tripToApollo),
    url(r'^moonQuiz$', views.doYouKnowMoon),
    url(r'^checkAnswers$', views.checkAnswers),
    url(r'^markMyTerritory$', views.markMyTerritory),
    url(r'^logout/$', views.logout),
    url(r'^login/$', views.login),

    #test urls
    url(r'^uploadImage$', views.uploadImage), #upload image on twitter
    url(r'^test$', views.authorizeAndShowFriends), #show twitter friends
    url(r'^t$', views.testView2),
    #url(r'^latestTweets$', views.latest_tweet),
    #url(r'^callBackUrl/', views.callBackView),
]
