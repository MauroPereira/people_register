from django.urls import path
from myapp.views import registro_persona

urlpatterns = [
    path('registro_persona/', registro_persona, name='registro_persona'),
]
