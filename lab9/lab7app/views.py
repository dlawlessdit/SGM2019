from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from lab7app.models import Book, BookInstance

# Create your views here.
class HomeView(TemplateView):
    def get(self, request, **kwargs):
        """View function for home page of site."""

    # Render the HTML template index.html 
        return render(request, 'index.html') 

class SecondView(TemplateView):
    def get(self, request, **kwargs):
        """View function for hthe second index of site with collapsible sidebar."""

    # Render the HTML template index2.html with the collapsible sidebar
        return render(request, 'index2.html') 

class BookView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book

class PageSelectView(TemplateView):
    def get(self, request, **kwargs):
        """View function for home page of site."""

    # Render the HTML template index.html 
        return render(request, 'pageselect.html')