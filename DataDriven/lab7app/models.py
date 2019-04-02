from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns


class HomePage(models.Model):
    """Model representing a page within an app, name must be unique to allow retieval of information"""
    name=models.CharField(max_length=20, unique=True)
    title= models.CharField(max_length=20,help_text="Enter the title of the page")
    desc=models.CharField(max_length=100, help_text="Enter a description of the page (will appear on the page")
    maincontent=models.CharField(max_length=300, help_text="Enter the main text that should appear on the page")
    mainimage = models.ImageField(upload_to = 'images/',null=True, blank=True, help_text="Upload the main image")
    shopimage = models.ImageField(upload_to = 'images/',null=True, blank=True, help_text="Upload the shopping image")
    drinkimage= models.ImageField(upload_to = 'images/',null=True, blank=True, help_text="Upload the drinking image")

    
    def __str__(self):
        """String for representing the Model object."""
        return self.name



