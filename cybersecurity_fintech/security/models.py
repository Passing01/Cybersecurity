from django.db import models

# Create your models here.
from django.db import models

class SecuredFile(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Nom du Fichier")
    upload_date = models.DateTimeField(auto_now_add=True, verbose_name="Date d'Ajout")
    encrypted_key = models.TextField(verbose_name="Clé de Chiffrement", blank=True, null=True)

    def __str__(self):
        return self.name

class Temoignage(models.Model):
    site_web = models.URLField(max_length=200)
    description = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.site_web

class Commentaire(models.Model):
    temoignage = models.ForeignKey(Temoignage, related_name='commentaires', on_delete=models.CASCADE)
    auteur = models.CharField(max_length=100)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.auteur} - {self.temoignage.site_web}'
