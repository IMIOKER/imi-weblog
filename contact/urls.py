from django.urls import path
from.views import *

app_name = 'cont'
urlpatterns = [
    path('', Cont, name='cont')
]