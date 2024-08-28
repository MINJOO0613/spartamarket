from django.shortcuts import render
from products.models import Product
from django.db.models import Q

# Create your views here.
def searchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__username__icontains=query)
        )
    return render(request, 'search.html', {'query': query, 'products': products})