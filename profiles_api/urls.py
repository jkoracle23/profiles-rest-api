#jk This is the place where url's for our api is stored
from django.urls import path, include
#include- this comes with django.urls module.This is used for including lists of URLs in the URL pattern and assiging the lists to a specific URL
from rest_framework.routers import DefaultRouter
from profiles_api import views


router=DefaultRouter()
router.register('hello-viewset', views.HelloViewSet,base_name='hello-viewset')#the first argument is the name of the URL that we wish to create.here we're going to access our API using hello view set
#The second argument is the view set that we wish to register to this URL
#Third argument is to be used for retrieving the URLs in our router .If we ever need to do that using the URL retrieving function provided by Django

urlpatterns=[
    path('hello-view/',views.HelloApiView.as_view()),
    path('',include(router.urls))#as you register new routes with our router it generates a list of URLs that are associated for our view set.it figures out the URLs that are required for all of the functions that we add to our view set and then it generates this URLs list which we can pass in to using the path function and the include function to our URL patterns.
#the reason we specify a blank string here is because we don't want to put a prefix to this URL we just want to include all of the URLs in the base of this URLs file
]
