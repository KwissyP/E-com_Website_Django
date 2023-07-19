"""
URL configuration for Projet_Final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from front.views import *
from user.views import *
from product.views import *
from blog.views import *
from contact.views import *
from cart.views import *
from wishlist.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('products/', product, name='product'),  # Vue pour afficher tous les produits
    path('products/<int:category_id>/', product, name='product_category'),  # Vue pour filtrer les produits par catégorie
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('connexion/', connexion, name='login'),
    path('inscription/', inscription, name='signup'),
    path('logout/', deco ),
    path('checkout/', checkout, name='checkout'),
    path('backoffice/', backoffice, name='backoffice'),
    path('user/destroy/<int:id>', destroy_User),
    path('user/edit/<int:id>', updateUser),
    path('back_product/', back_product, name='back_product'),
    path('product/edit/<int:id>', updateProduct),
    path('product/destroy/<int:id>', destroy_Product),
    path('create/product/', createProduct, name='create_Product'),
    path('product/<int:id>', readProduct, name='detail_Product'),
    path('back_article/', back_article, name='back_article'),
    path('article/edit/<int:id>', updateArticle),
    path('article/destroy/<int:id>', destroy_Article),
    path('create/article/', createArticle, name='create_article'),
    path('comment/create/<int:id>/', comment_create, name='comment_create'),
    path('contact/edit/<int:id>', updateContact),
    path('contact/destroy/<int:id>', destroy_Contact),
    path('back_contact/', back_contact, name='back_contact'),
    path('comment/create2/<int:id>/', comment_create2, name='comment_create2'),
    path('article/<int:id>', readArticle, name='detail_article'),
    path('cart/', view_cart, name='cart'),
    path('cart/add/', add_to_cart, name='add_to_cart'),
    path('update_cart/', update_cart, name='update_cart'),
    path('remove_from_cart/<int:product_id>/<str:size>/', remove_from_cart, name='remove_from_cart'),
    path('wishlist/<int:id>/', wishlist, name='add_to_wishlist'),
    path('myaccount/', my_account, name='my_account'),
    path('my-account/update/', update_account, name='update_account'),
    path('order_confirmation/<int:order_id>/', order_confirmation, name='order_confirmation'),
    path('orders/', order_list, name='order_list'),
    path('confirm/<int:order_id>/', confirm_order, name='confirm_order'),
    path('order_details/<int:order_id>/', order_details, name='order_details'),
    path('newsletter/', newsletter, name='newsletter'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
