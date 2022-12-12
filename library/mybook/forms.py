from dataclasses import field
from unittest.util import _MAX_LENGTH
from django import forms
from cartpage import models

class Shippingform(forms.ModelForm):
   class Meta:
       model = models.PurchasModel
       fields=['CName','CPhone','CMail','CAddress','CZipcode']

