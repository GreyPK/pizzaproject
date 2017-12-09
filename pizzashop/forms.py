from django import forms
from .models import *


class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=False)
    phone = forms.CharField(required=True)
    email = forms.EmailField(required=False)
    address = forms.CharField(required=False)

