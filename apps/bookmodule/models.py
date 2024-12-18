from django.db import models

class Address(models.Model):
    city = models.CharField(max_length=100)
    def _str_(self):
        return self.city

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address =  models.ForeignKey(Address,on_delete=models.CASCADE)

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)
    class Meta:
        app_label = 'bookmodule'