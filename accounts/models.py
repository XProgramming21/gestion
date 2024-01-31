from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.


class Tag(models.Model):
    nom = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nom


class Client(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    photo_profil = models.ImageField(null=True, blank=True)
    email = models.EmailField(max_length=254, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    CATEGORIES = (
        ("vetements", "vetements"),
        ("chaussures", "chaussures"),
        ("tshirt", "tshirt"),
    )

    nom = models.CharField(max_length=200, null=True)
    prix = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORIES)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.nom


class Commande(models.Model):
    STATUS = (("ECHEC", "ECHEC"), ("EN COURS", "EN COURS"), ("SUCCES", "SUCCES"))

    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    produit = models.ForeignKey(Produit, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.produit.nom
