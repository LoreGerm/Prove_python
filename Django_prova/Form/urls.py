from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='form'),
    path('mess', views.messaggi, name='mess'),
    path('mess/<int:id>/', views.elimina, name='elimina')
]
