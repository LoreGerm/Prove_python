
from django import forms
from matplotlib import widgets
from Form.models import utente

class FormMsg(forms.ModelForm):
    class Meta:
        model = utente
        fields = '__all__'
        
    widgets = {
        'nome': forms.TextInput(attrs={'class': 'form-control'}),
        'cognome': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'messaggio': forms.TextInput(attrs={'class': 'form-control'}),
    }

    
