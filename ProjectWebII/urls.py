from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import home

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('agenda/', include('agenda.urls')),
    path('horario/', include('horario.urls')),
    # path('offline/', cache_page(settings.PWA_APP_NAME)(pwa_view.offline)),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
