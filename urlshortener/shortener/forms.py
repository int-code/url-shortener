from django import forms
from .models import url_Model

class url_Form(forms.ModelForm):
    class Meta:
        model = url_Model
        fields = ['long_url']
        labels={
            'long_url':'Url'
        }