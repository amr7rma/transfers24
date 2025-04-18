from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(),name='index'),
    path('clubs/', ClubView.as_view(), name='clubs'),
    path('latest-transfers/', LatestTransfersView.as_view(), name='latest-transfers'),
    path('players/',PlayerView.as_view(), name='players'),
    path('playersu20/', Playersu20View.as_view(), name='playersu20'),
    path('stats/', StatsView.as_view(), name='stats'),
    path('stats/150-accurate-predictions/',AccuratePredictions150View.as_view(), name='stats-accurate-predictions'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


