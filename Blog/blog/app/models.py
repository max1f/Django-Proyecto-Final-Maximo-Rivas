from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,UserManager,BaseUserManager
from django.contrib.auth import get_user_model
from django.utils import timezone


User = get_user_model()
# Create your models here.

"""
class usuario(models.Model):
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f'Nombre: {self.username} - Contrasena: {self.password1} - E-Mail: {self.email}'
        """

class post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	timestamp = models.DateTimeField(default=timezone.now)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.content}'

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='blog/app/static/assets/img/home.jpg')

	def __str__(self):
		return f'Perfil de {self.user.username}'
