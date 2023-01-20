import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserPManager

class UserP(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, unique=True, max_length=8, default=uuid.uuid4, editable=False)
    username = models.CharField("Nombre de Usuario",max_length=150, unique=True)
    password = models.CharField("Contraseña", max_length=150)
    first_name = models.CharField("Nombre", max_length=150, blank=True)
    last_name = models.CharField("Apellido", max_length=150, blank=True)
    email = models.EmailField("Correo Electrónico", blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField("Fecha de Registro", default=timezone.now)

    objects = UserPManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = ("userp")
        verbose_name_plural = ("usersp")

