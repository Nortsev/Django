from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from mainapp.models import Product
from basketapp.models import Basket


def basket_add(request, product_id=None):
    product = get_object_or_404(Product, id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        basket = Basket(user=request.user, product=product)
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def basket_remove(requets):
    pass