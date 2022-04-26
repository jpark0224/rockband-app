from django.db import models

# Create your models here.


class Label(models.Model):
    name = models.CharField(max_length=30)
    founded_year = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
