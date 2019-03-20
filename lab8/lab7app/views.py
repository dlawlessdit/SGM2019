from django.shortcuts import render
from django.views.generic import TemplateView
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