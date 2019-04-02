from modeltranslation.translator import translator, TranslationOptions
from .models import  HomePage
#Indicate what fields translations are needed for by creating a class

class HomePageTranslationOptions(TranslationOptions):
    fields = ('title', 'desc', 'maincontent', 'mainimage', 'shopimage', 'drinkimage')


  #register the translation

translator.register(HomePage, HomePageTranslationOptions)

