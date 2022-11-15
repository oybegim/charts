from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trackerrr/', include('backend.urls')),
    path('ladaaa/', include('backend.urls')),
    path('bmvvv/', include('backend.urls')),
    path('ferrariii/', include('backend.urls')),
    path('davlattt/', include('backend.urls')),
    path('odammm/', include('backend.urls')),
]
