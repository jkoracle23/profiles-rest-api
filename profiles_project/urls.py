"""profiles_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #jk include is a function that you can use it to includes urls from the other apps in the root project url file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profiles_api.urls'))#when you go to forward slash api in the web server it will pass in the request to our django app which will then look up the URL patterns for the first URL which matches the URL that we've entered it will then pass in all of the URLs that match with the API URL and then it will load up the sub URLs in our  urls.py

]
