from email.policy import default
from pyexpat import model
from django.db import models
from mybook.models import Author, Book
from django.urls import reverse

from django.contrib.auth.models import User
# Create your models here.
class cartlist(models.Model):
    customer =models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)
    cart_id=models.CharField(max_length=250,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False)

    def get_url(self):
        return reverse('prod_cat')

    def __str__(self):
        return self.cart_id

    @property
    def get_cart_total(self):
        orderitems=self.items_set.all()
        total=sum([item.get_total for item in orderitems])

        return total

    @property
    def get_cart_items(self):
        orderitems=self.items_set.all()
        total=sum([item.quan for item in orderitems])
        return total

class items(models.Model):
    prodt=models.ForeignKey(Book,on_delete=models.SET_NULL,null=True,blank=True)
    cart=models.ForeignKey(cartlist,on_delete=models.SET_NULL, null=True, blank=True)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)

    def get_url(self):
        return reverse('details')

    # def __str__(self):
    #     return self.prodt

    @property
    def get_total(self):
        total=int(self.prodt.book_price )* self.quan

        return total




class PurchasModel(models.Model):
    customer=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
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
