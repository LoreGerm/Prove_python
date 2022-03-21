from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='form'),
    path('mess', views.messaggi, name='mess'),
    path('mess/<int:id>/', views.elimina, name='elimina'),
    path('update/<int:id>', views.update, name='update'),
    path('cerca', views.cerca, name='cerca'),
]
