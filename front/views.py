from django.shortcuts import get_object_or_404, redirect, render
from cart.models import Order
from user.models import User
from product.models import Product, Category
from blog.models import Article, CategoryArticle
from contact.models import Contact
from django.db.models import Count
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import render_to_string

# Create your views here.

def home(request):    
    contacts = Contact.objects.all()
    products = Product.objects.order_by('-id')[:6]
    popular_products = Product.objects.annotate(comment_count=Count('note')).order_by('-comment_count')[:6]
    latest_articles = Article.objects.all().order_by('-id')[:3]
    wishlist_products = None 
    if request.user.is_authenticated:
        wishlist_products = request.user.produits_wishlist.all()
    return render(request, 'Projet_Final/front/home.html', {'contacts' : contacts, 'products': products, 'popular_products': popular_products, 'latest_articles': latest_articles, 'wishlist_products': wishlist_products,})

def product(request, category_id=None):
    products = Product.objects.all()
    active_category = None
    wishlist_products = None 
    
    if request.user.is_authenticated:
        wishlist_products = request.user.produits_wishlist.all()
    
    if category_id is not None:
        category = Category.objects.get(id=category_id)
        products = products.filter(category=category)
        active_category = category
    
    categories = Category.objects.all()
    
    # Filtrage par taille
    selected_size = request.GET.get('size')
    if not selected_size:
        selected_size = 'S'  # Par défaut, la taille sélectionnée est 'S'
    
    sizes = ['S', 'M', 'L', 'XL', 'XXL']  # Liste des tailles disponibles
    
    if selected_size:
        products = products.filter(selected_size=selected_size)
    
    # Filtrage par taille pour la catégorie sélectionnée
    # if selected_size and active_category:
    #     products = products.filter(category=active_category, stock__contains={selected_size: True})
        
    for product in products:
        product.stock_quantity = product.get_stock_quantity(selected_size)
    
    paginator = Paginator(products, 12)  # Spécifiez le nombre de produits par page (ici, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'Projet_Final/front/products-left-sidebar-2.html', {
        'products': page_obj,
        'categories': categories,
        'active_category': active_category,
        'selected_size': selected_size,
        'sizes': sizes,  # Ajout de la variable 'sizes' dans le contexte
        'wishlist_products': wishlist_products,
    })




def blog(request):
    category_id = request.GET.get('category_id')
    search_query = request.GET.get('q')
    wishlist_products = None

    if category_id == "tous":
        articles = Article.objects.all()
    elif category_id is not None:
        category = CategoryArticle.objects.get(pk=category_id)
        articles = Article.objects.filter(category=category)
    else:
        articles = Article.objects.all()

    # Filtrer les articles en fonction du nom recherché (search_query)
    if search_query:
        articles = articles.filter(title__icontains=search_query)

    categories = CategoryArticle.objects.all()

    # Récupérer les articles avec le plus de commentaires
    popular_articles = Article.objects.annotate(comment_count=Count('note2')).order_by('-comment_count')[:3]
    
    if request.user.is_authenticated:
        wishlist_products = request.user.produits_wishlist.all()

    # Vérifier s'il y a des articles avec des commentaires
    if len(popular_articles) == 0:
        # Récupérer les trois premiers articles
        popular_articles = Article.objects.all()[:3]
        
    paginator = Paginator(articles, 6)  # Spécifiez le nombre de produits par page (ici, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Projet_Final/front/blog-5.html', {'articles': page_obj, 'categories': categories, 'popular_articles': popular_articles, 'wishlist_products': wishlist_products,})

def contact(request):
    contacts = Contact.objects.all()
    wishlist_products = None
    if request.user.is_authenticated:
        wishlist_products = request.user.produits_wishlist.all()
        
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Envoie de l'email de confirmation
        subject = 'Confirmation de réception de votre message'

        context = {'name': name}
        message = render_to_string('Projet_Final/front/confirmation_email.html', context)

        send_mail(subject, '', 'chrispandoulas@gmail.com', [email], html_message=message)
    
    return render(request, 'Projet_Final/front/contact.html', {'contacts' : contacts, 'wishlist_products': wishlist_products,})

def backoffice(request):
    users = User.objects.all()
    return render(request, 'Projet_Final/back/backoffice.html', {'users' : users,})

def back_product(request):
    products = Product.objects.all()
    return render(request, 'Projet_Final/back/back_product.html', {'products' : products,})

def back_article(request):
    articles = Article.objects.all()
    return render(request, 'Projet_Final/back/back_blog.html', {'articles' : articles,})

def back_contact(request):
    contacts = Contact.objects.all()
    return render(request, 'Projet_Final/back/back_contact.html', {'contacts' : contacts})

def order_list(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'Projet_Final/back/order_list.html', context)

def order_details(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    context = {
        'order': order
    }

    return render(request, 'Projet_Final/back/order_details.html', context)

def confirm_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    # Vérifier si la commande a déjà été confirmée
    if order.status == 'Confirmed':
        messages.error(request, 'This order has already been confirmed.')
        return redirect('order_list')
    
    # Confirmer la commande
    order.status = 'Confirmed'
    order.save()
    
    # Envoyer l'e-mail de confirmation à l'utilisateur
    send_mail(
        'Order Confirmation',
        'Your order has been confirmed.',
        'chrispandoulas@gmail.com',  # Remplacez par votre adresse e-mail
        [order.user.email],
        fail_silently=False,
    )
    
    messages.success(request, 'Order has been confirmed. Confirmation email has been sent to the user.')
    return redirect('order_list')