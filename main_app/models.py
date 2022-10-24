from django.db import models
from django import forms

class Person(models.Model):
    name = models.CharField(max_length=50)
    imgPath =  models.TextField(max_length=500)
    def __str__(self):
        return self.name

class Question(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    query = models.BooleanField(default=False)