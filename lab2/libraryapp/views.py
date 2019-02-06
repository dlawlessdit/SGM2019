from django.shortcuts import render
from django.views.generic import TemplateView
#Declare a dictionary with information about the books etc. which we will pass to index.html (before our class HomeView)
lib= {
'num_books': '3',
'num_authors': '3',
'num_instances': '10', #Number of book copies in total (across all books)
'num_instances_available': '7' #number of copies available to lend 
}

books = {"The Science of Discworld" : "Terry Pratchett", "Cacth 22" : "Joseph Heller", "The Lord of the Rings" : "J R R Tolkein" }


class HomeView(TemplateView):
    def get(self, request, **kwargs):
    	return render(request, 'index.html', {'details': lib}) 

class AuthorView(TemplateView):
    def get(self, request, **kwargs):
    	return render(request, 'authors.html', {'authors': books}) 

class BookView(TemplateView):
    def get(self, request, **kwargs):
    	return render(request, 'books.html', {'books': books}) 

class AboutView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'about.html', context=None)

