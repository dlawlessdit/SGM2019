from django.urls import path
# Import the views from our app
from lab7app.views import *

urlpatterns = [
    path('home', getDataHome, name='home'),
] 