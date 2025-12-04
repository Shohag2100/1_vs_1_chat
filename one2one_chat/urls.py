from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('messaging.urls')),
    path('api/', include('messaging.api_urls')),
]
