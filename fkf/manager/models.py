from django.db import models
from uuid import uuid4


# Create your models here.
class County(models.Model):
    """model to store county objects"""

    name = models.CharField(max_length=70, unique=True)
    admin = models.CharField(max_length=70, null=False)
    password = models.CharField(max_length=30, null=False)

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.admin, self.password)


class Academy(models.Model):
    """Defines the Academy object"""

    county = models.ForeignKey(County, on_delete=models.CASCADE)
    name = models.CharField(max_length=70, unique=True, null=False)
    admin = models.CharField(max_length=70, null=False)
    password = models.CharField(max_length=30, null=False)

    def __str__(self):
        return "{}, {}, {}, {}".format(
            self.name, self.county, self.admin, self.password
        )


class Player(models.Model):
    """Defines attributes of Player"""

    pid = str(uuid4())
    academy = models.ForeignKey(Academy, on_delete=models.CASCADE)
    name = models.CharField(max_length=70, null=False)

    def __str__(self):
        return "{}, {}, {}".format(self.pid, self.academy, self.name)
