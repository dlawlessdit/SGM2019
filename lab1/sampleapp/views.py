from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the home page of the app.")

def about(request):
    title = 'Software for the Global Market 2 2018-2019'
    author= 'Replace this with your name'
    html = '''<!DOCTYPE html>
    <html>
    <head>
      <title>''' + title + '''</title>
    </head>
    <body>
        <h1>About ''' + title + '''</h1>
        <p>This Website was developed by ''' + author + '''.</p>
    </body>
    </html>'''
    return HttpResponse(html)
