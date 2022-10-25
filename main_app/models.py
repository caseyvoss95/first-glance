from django.db import models
from django import forms
from django.contrib.auth.models import User


class Person(models.Model):
    name = models.CharField(max_length=50)
    imgPath =  models.TextField(max_length=500)
    def __str__(self):
        return self.name

class Question(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    option_names = models.CharField(max_length=50)
