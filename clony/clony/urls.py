from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from . import settings

from django.conf.urls import handler404
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("playground.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# print(settings.STATIC_URL, settings.STATIC_ROOT)