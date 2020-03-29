import os
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.defaults import page_not_found, server_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls'))
]

# FOR DEBUG ONLY
# ------------------------------------------------------------------------------
if settings.DEBUG and settings.MEDIA_ROOT:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)

if settings.DEBUG and settings.STATIC_URL:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_URL)

if settings.DEBUG:
    urlpatterns += [
        path(r'404/', page_not_found, {'exception': Exception('Testing - Not found')}, name='404'),
        path(r'500/', server_error, name='500'),
    ]

    if os.environ.get('ENABLE_DJANGO_TOOLBAR', True):
        import debug_toolbar

        urlpatterns += [
            path(r'__debug__/', include(debug_toolbar.urls))
        ]