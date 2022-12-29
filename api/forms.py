from django import forms

from . models import Books

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['image', 'title', 'category',  'description','author','publisher']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control'}),
            
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'title' : 'Enter books Name:',
            'image': 'Select an Image: ',
            'category': 'Select Category: ',
            'author': 'Enter author name: ',
            'description': 'Enter a Description: ',

        }