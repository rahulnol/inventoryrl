import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','inventory.settings')
import django
django.setup()

from django.contrib.auth import authenticate
from venue.models import NPVenue

from venue.serializer import NpVenueSerializer

def ram():

    venue = NPVenue.objects.get(id=2)
    venue_data = NpVenueSerializer(venue).data
    # print(venue_data['venue_timing'])
    # return
    # print (venue.venueimages_set.all())
    for a in venue_data['venue_timing']:
        print (type(a['time_start']))
ram()
