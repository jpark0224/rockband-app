from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

# Create your models here.


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instruments = ArrayField(ArrayField(
        models.CharField(max_length=30)), blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
