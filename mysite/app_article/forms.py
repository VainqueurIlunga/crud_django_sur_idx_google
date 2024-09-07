from django import forms
from .models import Article

class ArticleForme(forms.ModelForm):
    
    class Meta:
        model = Article     
        fields = ("title","price","description","image")
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'title': 'Titre',
            'price': 'Prix',
            'description': 'Description',
            'image': 'Image',
        }

