from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('accounts/', include('django.contrib.auth.urls')),  # Authentication (login, logout, password reset)
    path('', include('service_requests.urls')),  # Service requests app
    path('support/', include('support.urls')),  # Support app
    path('accounts/', include('accounts.urls')),

]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
