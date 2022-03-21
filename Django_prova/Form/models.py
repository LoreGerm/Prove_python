from django.db import models

# Create your models here.
class utente(models.Model):
    nome = models.CharField(max_length=50, null=False)
    cognome = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=100, null=False)
    messaggio = models.CharField(max_length=300, null=False)

    def __str__(self) -> str:
        return self.nome +' '+ self.cognome