from django.urls import path
from libraryapp.views import *


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about/',AboutView.as_view(), name='about'),
    path('books/',BookView.as_view(), name='books'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('authors/',AuthorView.as_view(), name='authors'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),
    path('testlang/', testlang, name='testlang'),

]
