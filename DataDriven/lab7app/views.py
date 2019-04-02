from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from lab7app.models import HomePage

# Create your views here.

def getDataHome(request):
    """View function for a data driven version home page of site."""
    #context = RequestContext(request)

    # Query the database for a list of a page called home
    # Order the categories by no. likes in descending order.
    # Add this to our context and call the page passing the context

    page_info = HomePage.objects.get(name="Home")#Find all content for the page
 
  
  
    pgcontext = {'page_info':page_info, }#make the images a dictionary
     # Render the response and send it back!
    
    return render(request, 'home.html', pgcontext)
 