from django.db import models

# Create your models here.

class infosTest(models.Model):
    date=models.DateTimeField((""), auto_now=False, auto_now_add=False),
    results=models.CharField(max_length=1000)
    
    
class formTest(models.Model):
    lien=models.CharField(max_length=40)
