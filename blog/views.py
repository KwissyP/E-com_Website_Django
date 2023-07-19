from django.shortcuts import render, redirect
from .models import Article, AnonymousUser2, CategoryArticle, Note2, Tag
from .forms import ArticleForm
from django.core.paginator import Paginator


# Create your views here.

def updateArticle(request,id):
    edit = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('back_article')
    else:
        form = ArticleForm(instance=edit)
        
    return render(request, 'Projet_Final/back/back_edit.html', {'form': form})

def destroy_Article(request, id):
    destroy = Article(id)
    destroy.delete()
    return redirect('back_article')

def createArticle(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('back_article')
    else:
        form = ArticleForm()
    return render(request, 'Projet_Final/back/back_edit.html', {"form": form})


def readArticle(request, id):
    wishlist_products = None
    if request.user.is_authenticated:
        wishlist_products = request.user.produits_wishlist.all()
    notes = Note2.objects.filter(article_id=id)
    show = Article.objects.get(id=id)
    categories = CategoryArticle.objects.all()  # Récupérer toutes les catégories
    tags = Tag.objects.all()  # Récupérer tous les tags
    return render(request, 'Projet_Final/front/single-blog-1.html', {"show": show, "notes": notes, "categories": categories, "tags": tags, 'wishlist_products': wishlist_products,})



def comment_create2(request, id):
    if request.method == 'POST':
        article = Article.objects.get(id=id)
        titre = request.POST.get('review-title')
        text = request.POST.get('texte')
        
        if request.user.is_authenticated:
            current_note = Note2.objects.create(
                author=request.user,
                article=article,
                titre=titre,
                text=text
            )
        else:
            name = request.POST.get('name')
            email = request.POST.get('email')
            
            anonymous_user = AnonymousUser2.objects.create(
                name=name,
                email=email
            )
            
            current_note = Note2.objects.create(
                anonymous_author=anonymous_user,
                article=article,
                titre=titre,
                text=text
            )
        
        # Redirection vers la page de détails de l'article
        return redirect('detail_article', id=article.id)
    
    return render(request, 'Projet_Final/front/single-blog-1.html')

