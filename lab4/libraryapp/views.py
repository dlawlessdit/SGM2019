from django.shortcuts import render, HttpResponse
from django.utils.translation import ugettext_lazy as _
from libraryapp.models import Book, Author, BookInstance, Genre
from django.views.generic import TemplateView, ListView, DetailView


def testlang(request):
    return HttpResponse(_('Welcome to the language bit!'))

def set_language(request):
    return render(request, 'set-language.html', {'LANGUAGES':settings.LANGUAGES,
                                                 'SELECTEDLANG':request.LANGUAGE_CODE})

class HomeView(TemplateView):
    def get(self, request, **kwargs):
        """View function for home page of site."""

    # Generate counts of some of the main objects
        num_books = Book.objects.all().count()
        num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
        num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
        num_authors = Author.objects.count()
    
        context = {
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
        }

    # Render the HTML template index.html with the data in the context variable
        return render(request, 'index.html', context=context) 

class BookView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book

class AuthorView(ListView):
    model =Author

class AuthorDetailView(DetailView):
    model = Author
    
class AboutView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'about.html', context=None)


from django import template
from django.urls import resolve, reverse, Resolver404
from django.utils.translation import get_language, activate

register = template.Library()
@register.simple_tag(takes_context=True)
def change_lang(context, lang=None, *args, **kwargs):
    """
    Get active page's url by a specified language
    Usage: {% change_lang 'en' %}
    """
    path = context['request'].path
    full_path = context['request'].get_full_path()
    try:
        url_parts = resolve(path)
        cur_language = get_language()
        try:
            activate(lang)
            url = reverse(url_parts.view_name, kwargs=url_parts.kwargs)
            activate(cur_language)
            parameters = "?{0}".format(full_path.split('?')[1]) if len(full_path.split('?')) == 2 else ""
            return "{0}{1}".format(url, parameters)
        except Exception:
            pass
    except Resolver404:
        pass
    return full_path