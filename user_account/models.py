from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from PIL import Image
# Create your models here.






# Create your models here.

#Model Manager 

class CustomUserManager(BaseUserManager):
	def create_user(self, email,username,password, **extra_fields):
		if not email:
			raise ValueError("email must be set")
		if not username:
			raise ValueError("username must be set ")
		email = self.normalize_email(email)
		username = username
		user = self.normalize_email(email)
		username = username
		user = self.model(email=email, username=username, **extra_fields)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self,email,username,password, **extra_fields):
		extra_fields.setdefault('is_staff',True)
		extra_fields.setdefault('is_superuser',True)
		extra_fields.setdefault('is_admin',True)
		if extra_fields.get('is_staff') is not True:
			raise ValueError('user must have is_staff set to True')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('user must have super user set to True')
		if extra_fields.get('is_admin') is not True:
			raise ValueError('user must have is admin set to True')
		return self.create_user(email,password,username, **extra_fields)

class Account(AbstractBaseUser,PermissionsMixin):
	email     = models.EmailField(unique=True)
	username  = models.CharField(max_length=100,unique=True)
	is_staff  = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)
	is_admin     = models.BooleanField(default=False)
	date_join    = models.DateTimeField(auto_now_add=True)
	last_login   = models.DateTimeField(auto_now=True)
	objects      = CustomUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def __str_(self):
		return self.username

class Profile(models.Model):
	user = models.OneToOneField(Account,on_delete=models.CASCADE)
	company_name = models.CharField(max_length=100,null=True,blank=True)
	company_profile = models.TextField(null=True,blank=True)
	company_profile = models.TextField(null=True,blank=True)
	official_email  = models.EmailField(null=True,blank=True)
	profile_picture = models.ImageField(default='profile_pics/default.jpg',upload_to='profile_pics',null=True,blank=True)
	
	



	def __str__(self):
		return self.user.username

	def save(self,*args, **kwargs):
		super().save()
		img = Image.open(self.profile_picture.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.profile_picture.path)
