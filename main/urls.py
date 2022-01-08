from django.urls import path
from.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home, name='home'),
    path('covid/', covid, name='covid'),
    path('shohada/', shohada, name='shoh'),
    path('shahr/', shahr, name='shahr'),
    path('det/<id>', Detail, name='det'),
    path('es', Es, name='es')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)