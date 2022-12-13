from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import Paginator
from .choices import price_choices, state_choices, bedroom_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    
    paginator = Paginator(listings, 2)
    page = request.GET.get('page')
    paged_listings= paginator.get_page(page)
    
    context = {
        'listings': paged_listings        
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing':  listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    
    #keywords
    # if 'keywords' in request.GET:
    keywords = request.GET.get("keywords")
    if keywords:
        queryset_list = queryset_list.filter(description__icontains = keywords)
    
    #city
    city = request.GET.get("city")
    if city:
        queryset_list = queryset_list.filter(city__iexact = city)
    
    #state
    state = request.GET.get("state")
    if state:
        queryset_list = queryset_list.filter(state__iexact = state)
    
    #bedrooms
    bedrooms = request.GET.get("bedrooms")
    if bedrooms:
        queryset_list = queryset_list.filter(bedrooms__lte = bedrooms)
    
    #price
    price = request.GET.get("price")
    if price:
        queryset_list = queryset_list.filter(price__lte = price)
    
    context ={
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)