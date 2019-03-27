from modeltranslation.translator import translator, TranslationOptions
from .models import Book
#Indicate what fields translations are needed for by creating a class
class BookTranslationOptions(TranslationOptions):
    fields = ('title', 'summary',)
  #register the translation
translator.register(Book, BookTranslationOptions)
