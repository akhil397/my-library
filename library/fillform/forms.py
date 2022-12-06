from django import forms
from fillform import models

class Shippingform(forms.ModelForm):
   class Meta:
       model = models.PurchasModel
       fields = "__all__"