
from django import forms
from Form.models import utente

class FormMsg(forms.ModelForm):
    class Meta:
        model = utente
        fields = '__all__'

    
