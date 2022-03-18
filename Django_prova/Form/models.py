from django.db import models

# Create your models here.
class utente(models.Model):
    nome = models.CharField(max_length=50, null='false')
    cognome = models.CharField(max_length=50, null='false')
    email = models.EmailField(max_length=100, null='false')
    messaggio = models.CharField(max_length=300, null='false')

    def __str__(self) -> str:
        return self.nome +' '+ self.cognome