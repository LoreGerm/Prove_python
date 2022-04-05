from rest_framework import serializers
from .models import utente

class UtenteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = utente
        fields = ('nome', 'cognome', 'email', 'messaggio')