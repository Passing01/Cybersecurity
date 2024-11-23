from security.models import *
from django.forms import ModelForm
from django import forms

class formEnter(forms.ModelForm):
    
    class Meta:
        model = formTest
        fields = ['lien']
        
class temoin(forms.ModelForm):
    
    class Meta:
        model = temoignage
        fields = '__all__'
        exclude=['pubDate']
        

