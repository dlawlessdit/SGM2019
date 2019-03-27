from django.contrib import admin



# Register your models here.
from lab7app.models import Book, BookInstance

admin.site.register(Book)
admin.site.register(BookInstance)
