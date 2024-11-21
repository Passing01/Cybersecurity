from security.models import formTest
from django.forms import ModelForm
from django import forms

class formEnter(forms.ModelForm):
    
    class Meta:
        model = formTest
        fields = ['lien',]
