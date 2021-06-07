from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.core.mail import send_mail
from .models import Contact

def store(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        agent_email = request.POST['agent_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/' + listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info.',
            None,
            [agent_email, 'ahmad.harminto@ngoding-bae.my.id'],
            fail_silently=False
        )

        messages.success(request, 'Your inquiry has been submitted, agent will get back to you soon')
        return redirect('/listings/' + listing_id)
