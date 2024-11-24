# forms.py
from django import forms
from .models import Temoignage, Commentaire

class TemoignageForm(forms.ModelForm):
    class Meta:
        model = Temoignage
        fields = ['site_web', 'description']

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['auteur', 'contenu']
