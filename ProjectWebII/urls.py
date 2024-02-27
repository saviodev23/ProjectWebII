from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import home
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path(r'', csrf_exempt(home), name="home"),
    path('agenda/', include('agenda.urls')),
    path('horario/', include('horario.urls')),
    path('bot/', include('bot.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)