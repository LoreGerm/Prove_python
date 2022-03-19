
from django import forms

from Form.models import utente

class FormMsg(forms.Form):
    nome = forms.CharField(max_length=100)
    cognome = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    messaggio = forms.CharField(widget=forms.Textarea)

    
