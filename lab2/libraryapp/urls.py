from django.urls import path
from libraryapp.views import *


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about/',AboutView.as_view(), name='about'),
    path('books/',BookView.as_view(), name='books'),
    path('authors/',AuthorView.as_view(), name='authors'),
]


