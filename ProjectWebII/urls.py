from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import home
<<<<<<< HEAD
from django.views.decorators.csrf import csrf_exempt
=======

>>>>>>> origin/savio
urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path(r'', csrf_exempt(home), name="home"),
    path('agenda/', include('agenda.urls')),
    path('horario/', include('horario.urls')),
<<<<<<< HEAD
    path('bot/', include('bot.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    # path('offline/', cache_page(settings.PWA_APP_NAME)(pwa_view.offline)),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> origin/savio
