import logging
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import getAvailableStates, getMaxPrice, getMaxBedroom
from .models import Listing

logger = logging.getLogger('django')

def index(request):
    listings = Listing \
        .objects \
        .order_by('-list_date') \
        .filter(is_published=True)
        
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'page': 'index',
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    imgs = []
    for i in range(1,7):
        if getattr(listing, f'photo_{i}'):
            imgs.append(getattr(listing, f'photo_{i}').url)

    context = {
        'listing': listing,
        'imgs': imgs
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    listings = Listing \
        .objects \
        .order_by('-list_date') \
        .filter(is_published=True)

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings = listings.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            listings = listings.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            listings = listings.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            listings = listings.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            listings = listings.filter(price__lte=price)
        
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

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
        'page': 'search',
        'filters': request.GET,
        'list_states': getAvailableStates().items(),
        'list_prices': list_prices.items(),
        'list_bedrooms': list_bedrooms.items(),
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)