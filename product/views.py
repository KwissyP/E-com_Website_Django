from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def updateProduct(request,id):
    edit = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('back_product')
    else:
        form = ProductForm(instance=edit)
    return render(request, 'Projet_Final/back/back_edit.html', {'form': form})

def destroy_Product(request, id):
    destroy = Product(id)
    destroy.delete()
    return redirect('back_product')

def createProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('back_product')
    else:
        form = ProductForm()
    return render(request, 'Projet_Final/back/back_edit.html', {"form": form})


def get_default_size(sizes, selected_size):
    available_sizes = ['S', 'M', 'L', 'XL', 'XXL']
    
    # Vérifier si la taille actuellement sélectionnée a encore du stock
    if selected_size in sizes and selected_size in available_sizes:
        return selected_size
    else:
        # Trouver la première taille disponible dans l'ordre "S", "M", "L", etc.
        for size in available_sizes:
            if size in sizes:
                return size
    # Si aucune taille n'est disponible, retourner la première taille de la liste
    return available_sizes[0]



def readProduct(request, id):
    notes = Note.objects.all().filter(product=id)
    show = Product.objects.get(id=id)
    sizes = [size for size in show.stock.keys() if show.get_stock_quantity(size) > 0]
    wishlist_products = None

    if request.user.is_authenticated:
        wishlist_products = request.user.produits_wishlist.all()

    selected_size = request.GET.get('size', 'S')  # Récupère la taille sélectionnée dans l'URL (par défaut 'S')

    # Mettre à jour le "selected_size" en fonction du stock disponible
    selected_size = get_default_size(sizes, selected_size)

    stock_quantity = show.get_stock_quantity(selected_size)

    # Tri des tailles dans l'ordre spécifié
    sizes = sorted(sizes, key=lambda x: ['S', 'M', 'L', 'XL', 'XXL'].index(x))

    return render(request, 'Projet_Final/front/products-type-1.html', {"show": show, "notes": notes, "sizes": sizes, "selected_size": selected_size, "stock_quantity": stock_quantity, 'wishlist_products': wishlist_products})


def comment_create(request, id):

    if request.method == 'POST':
        product = Product.objects.get(id=id)
        titre = request.POST.get('review-title')
        text = request.POST.get('texte')
        
        
        if request.user.is_authenticated:
            current_note = Note.objects.create(
                author=request.user,
                product=product,
                titre=titre,
                text=text
            )
        else:
            name = request.POST.get('name')
            email = request.POST.get('email')
            
            anonymous_user = AnonymousUser.objects.create(
                name=name,
                email=email
            )
            
            current_note = Note.objects.create(
                anonymous_author=anonymous_user,
                product=product,
                titre=titre,
                text=text
            )
        
        return redirect('detail_Product', id=id)
    
    return render(request, 'Projet_Final/front/products-type-1.html')
   
