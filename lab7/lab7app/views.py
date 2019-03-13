from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomeView(TemplateView):
    def get(self, request, **kwargs):
        """View function for home page of site."""

    # Render the HTML template index.html 
        return render(request, 'index.html') 