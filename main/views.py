from django.shortcuts import render
from django.views import View
from .models import *
from django.db.models import F, ExpressionWrapper, FloatField
from django.db.models.functions import Abs

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class ClubView(View):
    def get(self, request):
        clubs = Club.objects.all()
        context = {'clubs': clubs}
        return render(request, 'clubs.html', context)


class LatestTransfersView(View):
    def get(self, request):
        transfers = Transfer.objects.all()
        context = {'transfers': transfers}
        return render(request, 'latest-transfers.html', context)
class PlayerView(View):
    def get(self, request):
        players = Player.objects.all()
        context = {'players': players}
        return render(request, 'players.html', context)
class Playersu20View(View):
    def get(self, request):
        playersu20 = Player.objects.filter(age__lt=20)
        context = {'playersu20': playersu20}
        return render(request, 'U-20 players.html', context)
class StatsView(View):
    def get(self, request):
        return render(request, 'stats.html')

class AccuratePredictions150View(View):
    def get(self, request):
            transfers = Transfer.objects.annotate(
                accuracy_percent=ExpressionWrapper(
                    (Abs(F('price') - F('price_tft')) / F('price')) * 100,
                    output_field=FloatField()
                )
            ).order_by('accuracy_percent')[150:]

            context = {
                'transfers': transfers
            }
            return render(request, 'stats/150-accurate-predictions.html', context)

