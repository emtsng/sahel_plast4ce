from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = 'Sahel Plast4ce administration'
admin.site.site_title = 'Sahel Plast4ce'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.plast4ce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'apps.plast4ce.views.handler404'
