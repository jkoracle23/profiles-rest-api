#jk This is the place where url's for our api is stored
from django.urls import path
from profiles_api import views


urlpatterns=[
    path('hello-view/',views.HelloApiView.as_view()),
]
