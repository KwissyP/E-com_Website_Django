from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Order, OrderItem
from product.models import Product
from django.core.mail import send_mail
from django.db import transaction

def view_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.cartitem_set.all()
        
        # Calculer le sous-total de chaque élément du panier
        for cart_item in cart_items:
            cart_item.update_subtotal()
            
            # Calculer la quantité de stock pour le cart_item
            size = cart_item.size
            quantity = cart_item.product.get_stock_quantity(size)
            cart_item.stock_quantity = quantity
        
        # Calculer les frais de livraison
        shipping = 30.00
        
        # Calculer le sous-total
        subtotal = sum(cart_item.subtotal for cart_item in cart_items)
        
        # Calculer le total du panier    
        total = subtotal + shipping
        
    except Cart.DoesNotExist:
        cart_items = None
        total = 0
        shipping = 0
        subtotal = 0
        
    if request.user.is_authenticated:
        wishlist_products = request.user.produits_wishlist.all()
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'shipping': shipping,
        'subtotal': subtotal,
        'wishlist_products': wishlist_products,
    }
    
    return render(request, 'Projet_Final/front/cart.html', context)


def add_to_cart(request):
    product_id = request.GET.get('product_id')
    size = request.GET.get('size')
    quantity = int(request.GET.get('quantity', 1))
    
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product, size=size)
    
    if item_created:
        cart_item.quantity = quantity
    else:
        cart_item.quantity += quantity
        
    if request.user.is_authenticated:
        wishlist_products = request.user.produits_wishlist.all()
    
    # Vérifier si la quantité ne dépasse pas le stock disponible pour la taille sélectionnée
    stock_quantity = product.get_stock_quantity(size)  # Récupérer la quantité de stock pour la taille sélectionnée
    if cart_item.quantity > stock_quantity:
        cart_item.quantity = stock_quantity
    
    cart_item.save()
    
    # Mettre à jour le sous-total du CartItem
    cart_item.update_subtotal()
    
    messages.success(request, f"{product.name} added to cart.")
    
    return redirect('cart')

def remove_from_cart(request, product_id, size):
    cart = Cart.objects.get(user=request.user)
    product = Product.objects.get(id=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product, size=size)
    cart_item.delete()
    return redirect(request.META['HTTP_REFERER'])

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required



@login_required
def checkout(request):
    wishlist_products = request.user.produits_wishlist.all()
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cartitem_set.all()
    
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    shipping_cost = 30.00
    total = subtotal + shipping_cost
    
    order = None
    
    if request.method == 'POST':
        with transaction.atomic():
            # Créer une nouvelle instance de Order
            order = Order.objects.create(
                user=request.user,
                cart=cart,
                total_amount=total,
            )
            
            # Créer les instances de OrderItem pour chaque produit du panier
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    size=item.size,
                    quantity=item.quantity,
                )
            
            # Vider le panier
            cart.cartitem_set.all().delete()
            
            # Envoyer l'e-mail de confirmation à l'utilisateur
            send_mail(
                'Order Confirmation',
                'Thank you for your order!',
                'Xton@gmail.com',
                [request.POST['email']],
                fail_silently=False,
            )
            
            messages.success(request, 'Your order has been placed. A confirmation email has been sent.')
            
            return redirect('order_confirmation', order_id=order.pk)
    
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping_cost': shipping_cost,
        'total': total,
        'wishlist_products': wishlist_products,
        'order': order,
    }
    
    return render(request, 'Projet_Final/front/checkout.html', context)


@login_required
def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id)
    order_items = order.order_items.all()
    
    send_mail(
        'Order Confirmation',
        'Your order has been confirmed by the admin.',
        'Xton@gmail.com',
        [order.user.email],
        fail_silently=False,
    )
    
    context = {
        'order': order,
        'order_items': order_items,
    }
    
    return render(request, 'Projet_Final/front/order_confirmation.html', context)


@login_required
def update_cart(request):
    if request.method == 'POST':
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.cartitem_set.all()
        
        for cart_item in cart_items:
            quantity_key = f'quantity_{cart_item.id}'
            new_quantity = int(request.POST.get(quantity_key))
            
            # Vérifier si la nouvelle quantité est valide
            stock_quantity = cart_item.product.get_stock_quantity(cart_item.size)
            if new_quantity > stock_quantity:
                messages.warning(request, f"Invalid quantity for {cart_item.product.name}. Maximum available quantity: {stock_quantity}")
            else:
                cart_item.quantity = new_quantity
                cart_item.update_subtotal()
                cart_item.save()
        
        messages.success(request, "Cart updated successfully.")
    
    if request.user.is_authenticated:
        wishlist_products = request.user.produits_wishlist.all()
    
    return redirect('cart')