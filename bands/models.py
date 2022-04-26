from django.db import models
from django.contrib.postgres.fields import ArrayField
from labels.models import Label
from members.models import Member
from django.contrib.auth.models import User

# Create your models here.


class Band(models.Model):
    name = models.CharField(max_length=50)
    genres = ArrayField(ArrayField(
        models.CharField(max_length=30)), blank=True)
    origin = models.CharField(max_length=70)
    year_formed = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, null=True)

    leader = models.ForeignKey(
        Member, on_delete=models.SET_NULL, null=True, blank=True, related_name="starred")

    label = models.ForeignKey(
        Label, null=True, blank=True, on_delete=models.SET_NULL, related_name="managed_bands")

    members = models.ManyToManyField(
        Member, blank=True, related_name="supported")

    author = models.ForeignKey(
        User, related_name="bands", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name} is a band formed in {self.origin} in {self.year_formed}. Their genre(s) include {self.genres}."


class Album(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.band}"
