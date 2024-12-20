from django.db import models

class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

# Lab 8 and 10 Models 
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
    description = models.TextField(blank=True, null=True)
    class Meta:
        app_label = 'bookmodule'

class Address2(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)

class Student2(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    addresses = models.ManyToManyField(Address2)

"""
# Lab 7 and 9 Model

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
        
"""