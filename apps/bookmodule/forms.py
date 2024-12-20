from django import forms
from .models import Book, Address, Student


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city']
        widgets = {
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'address']
