from django.db import models



class Person(models.Model):
    name = models.CharField(max_length=50)
    imgPath =  models.CharField(max_length=100)
    def __str__(self):
        return self.name




class Photo(models.Model):
    url = models.CharField(max_length=200)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for person_id {self.person_id} @{self.url}"