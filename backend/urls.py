from django.urls import path
from .views import *

urlpatterns = [
    path('trackerrr/', trackerr),
    path('lada/', lada),
    path('bmvvv/', bmvv),
    path('ferrariii/', ferrarii),
    path('davlattt/', davlatt),
    path('odammm/', odamm)
]