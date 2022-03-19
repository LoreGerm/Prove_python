
from django import forms

from Form.models import utente

class FormMsg(forms.Form):
    nome = forms.CharField()
    cognome = forms.CharField()
    email = forms.EmailField()
    messaggio = forms.Textarea()

    
