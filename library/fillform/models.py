from django.db import models

# Create your models here.
class PurchasModel(models.Model):
    CName=models.CharField(max_length=30)
    CPhone=models.CharField(max_length=10)
    CMail=models.EmailField()
    CAddress=models.CharField(max_length=50)
    CDistric=models.CharField(max_length=100,default="")
    CBranch=models.CharField(max_length=100, default="")
    CZipcode=models.CharField(max_length=6)
    Ddate=models.DateField()
    Dtime=models.TimeField()
    def __str__(self):
         return '{}'.format(self.CName)