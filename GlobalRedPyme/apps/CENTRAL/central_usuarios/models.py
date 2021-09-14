from djongo import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from apps.CENTRAL.central_roles.models import Roles


def upload_path(instance, filname):
    return '/'.join(['CENTRAL/imgUsuarios', str(instance.username) + "_" + filname])

# Create your models here.


class Usuarios(AbstractBaseUser):
    _id = models.ObjectIdField()
    username = models.CharField(blank=True, null=True,max_length=150, unique=True)
    imagen = models.ImageField(blank=True, null=True, upload_to=upload_path)
    nombres = models.CharField(max_length=150,blank=True, null=True)
    apellidos = models.CharField(max_length=250,blank=True, null=True)
    email = models.CharField(max_length=250,blank=True, null=True, unique=True)
    estado = models.CharField(max_length=200,blank=True, null=True)
    roles = models.ForeignKey(Roles, null=False, on_delete=models.CASCADE)  # Relacion Rol
    pais = models.CharField(max_length=200,blank=True, null=True)
    telefono = models.CharField(max_length=30,blank=True, null=True)
    whatsapp = models.CharField(max_length=30,blank=True, null=True)
    compania = models.CharField(max_length=200,blank=True, null=True)
    twitter = models.CharField(max_length=200,blank=True, null=True)
    facebook = models.CharField(max_length=200,blank=True, null=True)
    instagram = models.CharField(max_length=200,blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    state = models.SmallIntegerField(default=1)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    