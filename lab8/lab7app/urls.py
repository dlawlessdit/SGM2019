from django.urls import path
# Import the views from our app
from lab7app.views import *


# Set up a path to our index page, this is our default. If http://127.0.0.1:8000/lab7 is requested 
#then the request will be cause HomeView in our views.py to be executed
#We are also setting up a shorthand reference to this page that we can use for linking in our templates - this page is going to index

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('sidebar', SecondView.as_view(), name='index2'),

] 