from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from chat.views import home
from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page route
    # Your other URL patterns here
]

if settings.DEBUG:  # Only serve static and media files in development
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
