from django.db import models
from uuid import uuid4
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class MyUserManager(BaseUserManager):
    def create_user(
        self, name, role, is_staff=False, is_superuser=False, password=None
    ):
        """
        Creates and saves a User with the given data
        """
        if not name:
            raise ValueError("Users must have a name")

        user = self.model(
            name=name,
            role=role,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password, role):
        """
        Creates and saves a superuser with the given data
        """
        u = self.create_user(name, role, True, True, password)
        u.is_admin = True
        u.save(using=self._db)
        return u


class Admin(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=70, unique=True)
    role = models.CharField(max_length=30, null=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MyUserManager()
    USERNAME_FIELD = "name"
    ROLE_FIELD = "role"
    REQUIRED_FIELDS = ["role"]

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class County(models.Model):
    """model to store county objects"""

    name = models.CharField(max_length=70, unique=True)
    password = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name


class Academy(models.Model):
    """Defines the Academy object"""

    county = models.ForeignKey(County, on_delete=models.CASCADE)
    name = models.CharField(max_length=70, unique=True, null=False)
    password = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name


class Player(models.Model):
    """Defines attributes of Player"""

    pid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    academy = models.ForeignKey(Academy, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    picture = models.ImageField(
        null=True,
        blank=True,
        validators=[FileExtensionValidator(["png", "jpg", "jpeg"])],
        upload_to="images/",
    )

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.pid, self.academy)
