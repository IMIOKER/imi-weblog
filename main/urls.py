from django.urls import path
from.views import *

urlpatterns = [
    path('', Home, name='home'),
    path('covid/', covid, name='covid'),
    path('shohada/', shohada, name='shoh'),
    path('shahr/', shahr, name='shahr'),
    path('det/<id>', Detail, name='det'),
    path('es', Es, name='es')
]