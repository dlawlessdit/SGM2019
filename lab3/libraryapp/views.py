from django.shortcuts import render, HttpResponse
from django.utils.translation import ugettext_lazy as _

from django.views.generic import TemplateView
#Declare a dictionary with information about the books etc. which we will pass to index.html
lib= {
'num_books': '3',
'num_authors': '3',
'num_instances': '10', #Number of book copies in total (across all books)
'num_instances_available': '7' #number of copies available to lend 
}

books = {"The Science of Discworld" : "Terry Pratchett", "Cacth 22" : "Joseph Heller", "The Lord of the Rings" : "J R R Tolkein" }
def testlang(request):
    return HttpResponse(_('Welcome to the language bit!'))

def set_language(request):
    return render(request, 'set-language.html', {'LANGUAGES':settings.LANGUAGES,
                                                 'SELECTEDLANG':request.LANGUAGE_CODE})

class HomeView(TemplateView):
    def get(self, request, **kwargs):
    	return render(request, 'index.html', {'details': lib}) 


class BookView(TemplateView):
    def get(self, request, **kwargs):
    	return render(request, 'books.html', {'books': books}) 

class AuthorView(TemplateView):
    def get(self, request, **kwargs):
    	return render(request, 'authors.html', {'authors': books}) 
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