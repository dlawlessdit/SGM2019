from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomeView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class AboutView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'about.html', context=None)

