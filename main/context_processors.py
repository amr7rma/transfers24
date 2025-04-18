from .models import *
from django.db.models import Count
def get_countries(request):
    countries = Country.objects.annotate(club_count=Count('club')).filter(club_count__gt=0)
    l=countries.count()
    if l%2==1:
        countries_left= countries[:l // + 1],
        countries_right= countries[l // + 1:]
    else:
        countries_left = countries[:l // 2],
        countries_right = countries[l // 2:]
    context = {
        'countries_left': countries_left,
        'countries_right': countries_right
    }
    return context