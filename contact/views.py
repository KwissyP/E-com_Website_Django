from django.shortcuts import render,redirect
from .models import Contact
from .forms import ContactForm
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def updateContact(request,id):
    edit = Contact.objects.get(id=id)
    if request.user.is_authenticated:
        wishlist_products = request.user.produits_wishlist.all()
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('back_contact')
    else:
        form = ContactForm(instance=edit)
    return render(request, 'Projet_Final/back/back_edit.html', {'form': form, 'wishlist_products': wishlist_products,})

def destroy_Contact(request, id):
    destroy = Contact(id)
    destroy.delete()
    return redirect('back_contact')

def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Valider l'e-mail ici (vous pouvez utiliser des outils de validation intégrés ou des bibliothèques externes)

        # Envoie de l'e-mail de confirmation
        subject = 'Confirmation de réception de votre inscription à la newsletter'
        context = {'email': email}
        message = render_to_string('Projet_Final/front/newsletter.html', context)

        send_mail(subject, '', settings.DEFAULT_FROM_EMAIL, [email], html_message=message)

    return redirect(request.META['HTTP_REFERER'])