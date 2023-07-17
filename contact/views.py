from django.shortcuts import render,redirect
from .models import Contact
from .forms import ContactForm

# Create your views here.

def updateContact(request,id):
    edit = Contact.objects.get(id=id)
    if request.user.is_authenticated:
        wishlist_products = request.user.produits_wishlist.all()
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('back_Contact')
    else:
        form = ContactForm(instance=edit)
    return render(request, 'Projet_Final/back/back_edit.html', {'form': form})

def destroy_Contact(request, id):
    destroy = Contact(id)
    destroy.delete()
    return redirect('back_Contact')