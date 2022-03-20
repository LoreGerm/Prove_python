from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='form'),
    path('mess', views.messaggi, name='mess'),
    path('eli/<utente_id>', views.elimina, name='elimina')
]
