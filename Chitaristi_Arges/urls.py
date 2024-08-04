# Chitaristi_Arges/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from chitaristi.admin import chitaristi_admin_site  # Importă site-ul admin personalizat
from chitaristi.views import CustomAdminLoginView

urlpatterns = [
    path('admin/', chitaristi_admin_site.urls),  # Folosește site-ul de admin personalizat
    path('', include('chitaristi.urls')),  # Include URL patterns from the 'chitaristi' app
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
