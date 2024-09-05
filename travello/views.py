from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination


def index(request):
    
    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.desc = "Sunny sunny beach"
    dest1.img = "destination_1.jpg"
    dest1.price = 360
    dest1.offer = False
    
    
    dest2 = Destination()
    dest2.name = "Indonesia"
    dest2.desc = "Tropical paradise"
    dest2.img = "destination_2.jpg"
    dest2.price = 800
    dest2.offer = True
    
    
    dest3 = Destination()
    dest3.name = "San Francisco"
    dest3.desc = "Large red bridge"
    dest3.img = "destination_3.jpg"
    dest3.price = 360
    dest3.offer = False
    
    dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'dests': dests })

