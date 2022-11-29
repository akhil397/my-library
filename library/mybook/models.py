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
    author_age = IntegerField()
    def __str__(self):
         return '{}'.format(self.author_name)


class Book(models.Model):
    book_name = models.CharField(max_length=20)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
         return '{}'.format(self.book_name)


class PurchasModel(models.Model):
    CName=models.CharField(max_length=30)
    CPhone=models.CharField(max_length=10)
    CMail=models.EmailField()
    CAddress=models.CharField(max_length=50)
    CDistric=models.ForeignKey(District,on_delete=models.CASCADE)
    CBranch=models.ForeignKey(Branches,on_delete=models.CASCADE)
    CZipcode=models.CharField(max_length=6)
    BName=models.CharField(max_length=30)
    Bquatity=models.IntegerField()
    Ddate=models.DateField()
    Dtime=models.TimeField()
    def __str__(self):
         return '{}'.format(self.CName)

