from django.db import models

# Create your models here.

class infosTest(models.Model):
    date=models.DateTimeField("", auto_now=False, auto_now_add=False),
    results=models.CharField(max_length=1000)
    
    
class formTest(models.Model):
    lien=models.EmailField(max_length=50)
    
class temoignage(models.Model):
    Nom=models.CharField("Votre nom", max_length=50),
    Prenom=models.CharField("Votre Prenom", max_length=50),
    Message=models.CharField("Site malicieux", max_length=5000),
    PubDate=models.DateTimeField("Date de publication", auto_now=False, auto_now_add=False)
