import logging
from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from listings.choices import getAvailableStates, getMaxPrice, getMaxBedroom
from agents.models import Agent

logger = logging.getLogger('django')

def index(request):
    listings = Listing \
        .objects \
        .order_by('-list_date') \
        .filter(is_published=True)[:3]

    list_prices = dict();
    list_bedrooms = dict();
    max_price = getMaxPrice();
    max_bedroom = getMaxBedroom()
    if not max_price:
        max_price = 1000000
    if not max_bedroom:
        max_bedroom = 5
    
    i = 50000
    while (i <= max_price + 100000):
        list_prices[str(i)] = i
        i += 100000

    i = 1
    while (i <= max_bedroom):
        list_bedrooms[str(i)] = i
        i += 1

    context = {
        'list_states': getAvailableStates().items(),
        'list_prices': list_prices.items(),
        'list_bedrooms': list_bedrooms.items(),
        'listings': listings
    }
    
    return render(request, 'pages/index.html', context)

def about(request):
    agents = Agent \
        .objects \
        .order_by('-hire_date')

    mvps = Agent \
        .objects \
        .all() \
        .filter(is_mvp=True)

    context = {
        'agents': agents,
        'mvps': mvps
    }

    return render(request, 'pages/about.html', context)
