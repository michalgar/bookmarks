from django import forms
#from django.forms import ModelForm
from .models import Books

class AddBookForm(forms.Form):
    book_title = forms.CharField(label='Book Name', max_length=100)
    author = forms.CharField(label='Author', max_length=40)
    description = forms.CharField(widget=forms.Textarea)


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        exclude = ('owner',)
        #fields = '__all__'
