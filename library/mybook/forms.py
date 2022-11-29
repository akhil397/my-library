from dataclasses import field
from unittest.util import _MAX_LENGTH
from django import forms
from mybook import models

class Purchaseform(forms.ModelForm):
   class Meta:
       model = models.PurchasModel
       fields = "__all__"