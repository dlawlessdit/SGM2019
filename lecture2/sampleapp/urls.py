from django.urls import path
from sampleapp.views import *

urlpatterns = [
    path('', HomeView.as_view()),
    path('about/', AboutView.as_view()),
]



