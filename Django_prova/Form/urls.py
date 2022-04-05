from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'utente', views.UtenteViewsSet)

urlpatterns = [
    path('', views.aggiungi, name='aggiungi'),
    path('mess', views.messaggi, name='mess'),
    path('mess/<int:id>/', views.elimina, name='elimina'),
    path('update/<int:id>', views.update, name='update'),
    path('cerca', views.cerca, name='cerca'),

    path('api', include(router.urls)),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework') )
]
