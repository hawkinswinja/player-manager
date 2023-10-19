from django.db import models
from uuid import uuid4
from django.core.validators import FileExtensionValidator


class County(models.Model):
    """model to store county objects"""

    name = models.CharField(max_length=70, unique=True)
    admin = models.CharField(max_length=70, null=False)
    password = models.CharField(max_length=30, null=False)

    def __str__(self):
        return "{}".format(self.name)


class Academy(models.Model):
    """Defines the Academy object"""

    county = models.ForeignKey(County, on_delete=models.CASCADE)
    name = models.CharField(max_length=70, unique=True, null=False)
    admin = models.CharField(max_length=70, null=False)
    password = models.CharField(max_length=30, null=False)

    def __str__(self):
        return "{}, {}".format(self.name, self.county)


class Player(models.Model):
    """Defines attributes of Player"""

    pid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    academy = models.ForeignKey(Academy, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    picture = models.ImageField(
        validators=[FileExtensionValidator(["png", "jpg", "jpeg"])]
    )

    def __str__(self):
        return "{}, {}, {}".format(self.pid, self.academy, self.name)
