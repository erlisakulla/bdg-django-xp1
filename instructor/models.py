<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)

# Create your models here.

class MyUserManager(BaseUserManager):
	def create_user(self, email, full_name, password=None):
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email=self.normalize_email(email),
			full_name=full_name,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, full_name, password):
		user = self.create_user(
			email,
			password=password,
			full_name=full_name,
		)
		user.is_admin = True
		user.save(using=self._db)
		return user

class InstructorUser(AbstractBaseUser):
	full_name = models.CharField(max_length=50)
	email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
	
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['full_name']

	def __str__(self):
		return self.full_name

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.is_admin
=======
from django.db import models


# Create your models here.

class Instructor(models.Model):
	full_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	password = models.CharField(max_length=32)

	def __str__(self):
		return self.full_name
>>>>>>> ce29bf3716dd0ce95bd0600ec0cc41dbd2acf737
