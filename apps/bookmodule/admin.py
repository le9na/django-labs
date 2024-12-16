from django.contrib import admin
from .models import Book, Student, Address
# Register your models here.
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Address)
