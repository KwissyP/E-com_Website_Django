from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from product.models import Product

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
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'shipping': shipping,
        'subtotal': subtotal,
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


def checkout(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cartitem_set.all()
    
    # Calcul du sous-total
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    
    # Calcul des frais de livraison
    shipping_cost = 30.00  # Mettez ici le montant réel des frais de livraison
    
    # Calcul du total de la commande
    total = subtotal + shipping_cost
    
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping_cost': shipping_cost,
        'total': total,
    }
    
    return render(request, 'Projet_Final/front/checkout.html', context)

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
    
    return redirect('cart')