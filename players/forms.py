from django import forms
from models import player

class PlayerForm(forms.ModelForm):
    
    class Meta:
        model = player

 
