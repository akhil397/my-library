from tkinter import CASCADE
from tokenize import Name
from django.db import models
from django.forms import IntegerField  
#user booko pasd 2345
class District(models.Model):  
    DICSTRINM= models.CharField(max_length=15)  
    def __str__(self):
         return '{}'.format(self.DICSTRINM)
class Branches(models.Model):
    BRANCHNM= models.CharField(max_length=15)  
    DistricNM = models.ForeignKey(District, on_delete=models.CASCADE)
    def __str__(self):
         return '{}'.format(self.BRANCHNM)
   

class Author(models.Model):
    author_name = models.CharField(max_length=20)
    auther_desc=models.TextField(blank=True)
    auther_image=models.ImageField(upload_to='auther',blank=True)
    author_age = IntegerField()
    def __str__(self):
         return '{}'.format(self.author_name)


class Book(models.Model):
    book_name = models.CharField(max_length=20)
    book_price=models.DecimalField(max_digits=10,decimal_places=2)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_image=models.ImageField(upload_to='books',blank=True)
    desc=models.TextField(null=False)
    stock=models.IntegerField(null=False)
    available=models.BooleanField(default=True)

    def __str__(self):
         return '{}'.format(self.book_name)
