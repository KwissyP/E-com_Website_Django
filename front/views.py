from django.shortcuts import render
from user.models import User
from product.models import Product, Category
from blog.models import Article, CategoryArticle
from contact.models import Contact
from django.db.models import Count
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        wishlist_products = request.user.produits_wishlist.all()
    contacts = Contact.objects.all()
    products = Product.objects.order_by('-id')[:6]
    popular_products = Product.objects.annotate(comment_count=Count('note')).order_by('-comment_count')[:6]
    latest_articles = Article.objects.all().order_by('-id')[:3]
    return render(request, 'Projet_Final/front/home.html', {'contacts' : contacts, 'products': products, 'popular_products': popular_products, 'latest_articles': latest_articles})

def product(request, category_id=None):
    products = Product.objects.all()
    active_category = None
    
    if request.user.is_authenticated:
        wishlist_products = request.user.produits_wishlist.all()
    
    if category_id is not None:
        category = Category.objects.get(id=category_id)
        products = products.filter(category=category)
        active_category = category
    
    categories = Category.objects.all()
    
    # Filtrage par taille
    selected_size = request.GET.get('size')
    if selected_size:
        products = products.filter(selected_size=selected_size)
    
    # Filtrage par taille pour la catégorie sélectionnée
    if selected_size and active_category:
        products = products.filter(category=active_category, stock__contains={selected_size: True})
    
    paginator = Paginator(products, 12)  # Spécifiez le nombre de produits par page (ici, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'Projet_Final/front/products-left-sidebar-2.html', {
        'products': page_obj,
        'categories': categories,
        'active_category': active_category,
        'selected_size': selected_size,
        'sizes': ['S', 'M', 'L', 'XL', 'XXL'],  # Liste des tailles disponibles
        'wishlist_products': wishlist_products,
    })


def blog(request):
    category_id = request.GET.get('category_id')
    search_query = request.GET.get('q')

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

    return render(request, 'Projet_Final/front/blog-5.html', {'articles': page_obj, 'categories': categories, 'popular_articles': popular_articles})


def contact(request):
    contacts = Contact.objects.all()
    if request.user.is_authenticated:
        wishlist_products = request.user.produits_wishlist.all()
    return render(request, 'Projet_Final/front/contact.html', {'contacts' : contacts})

def checkout(request):
    if request.user.is_authenticated:
        wishlist_products = request.user.produits_wishlist.all()
    return render(request, 'Projet_Final/front/checkout.html')

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