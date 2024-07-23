from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

TYPE_USER = (("Etudiant", "Édutiant(e)"), ("Universite", "Université"))

# Create your models here.


class CustomUser(AbstractUser):
    """User Model"""

    profil_picture = models.ImageField(upload_to="media", default="profilpic.png")
    type_user = models.CharField(max_length=10, choices=TYPE_USER, default="Etudiant")
    adress = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(
        max_length=20, blank=True, validators=[MinLengthValidator(10)]
    )
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )

    def __str__(self) -> str:
        return self.username
