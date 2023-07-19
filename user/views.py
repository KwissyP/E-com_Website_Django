from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from cart.models import Order
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

# Create your views here.

def inscription(request):
    if request.method == 'POST':
        username = request.POST['username']
        img_url = request.POST['img_url']
        password = request.POST['password']
        email = request.POST['email']
        
        # Créer l'utilisateur avec le rôle "Member"
        role = Role.objects.get(value='Member')
        user = User(username=username, password=make_password(password), email=email, img_url=img_url, role=role)
        user.save()
        
        # Info du mail
        subject = 'Bienvenue sur notre site'
        message = 'Merci de vous être inscrit à notre site.'
        from_email = 'chrispandoulas@gmail.com'
        to_email = user.email
        
        # Envoi du mail
        send_mail(subject, message, from_email, [to_email])
        
        login(request, user)
        return redirect('home')
    
    return render(request, 'Projet_Final/front/signup.html')

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'Projet_Final/front/login.html')

def deco(request):
    logout(request)
    return redirect('home')

def updateUser(request,id):
    edit = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('backoffice')
    else:
        form = UserForm(instance=edit)
    return render(request, 'Projet_Final/back/back_edit.html', {'form': form})

def destroy_User(request, id):
    destroy = User(id)
    destroy.delete()
    return redirect('backoffice')

def my_account(request):
    if not request.user.is_authenticated:
        return redirect('login')

    user_orders = Order.objects.filter(user=request.user)
    form = UserForm(instance=request.user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
        'user_orders': user_orders
    }

    return render(request, 'Projet_Final/front/myaccount.html', context)


def update_account(request):
    user = request.user
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        
        if form.is_valid():
            form.save()
            return redirect('my_account')
    else:
        form = UserForm(instance=user)
    
    return render(request, 'Projet_Final/front/update_account.html', {'form': form})

class CustomPasswordResetView(PasswordResetView):
    template_name = 'Projet_Final/front/password_reset.html'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'Projet_Final/front/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'Projet_Final/front/password_reset_confirm.html'
    
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'Projet_Final/front/password_reset_complete.html'