from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('IntegritasTecnica.apps.users.urls')),
    path('', include('IntegritasTecnica.apps.home.urls')),
    path('api/auth/login/', obtain_auth_token, name='login'),
    path('api/users/', include('IntegritasTecnica.apps.users.api.urls')),

]

# Allows to serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
