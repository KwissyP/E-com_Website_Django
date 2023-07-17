from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from product.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def wishlist(request, id):
    product = Product.objects.get(id=id)
    user = request.user
    
    if product in user.produits_wishlist.all():
        user.produits_wishlist.remove(product)
        
    else:
        user.produits_wishlist.add(product)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))