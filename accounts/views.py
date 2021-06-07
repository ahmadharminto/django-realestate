from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from contacts.models import Contact

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('dashboard')

        messages.error(request, 'These credentials do not match our records')
        return redirect('login')

    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if (User.objects.filter(email=email).exists()):
            messages.error(request, 'Email has already been taken')
            return redirect('register')

        if (User.objects.filter(username=username).exists()):
            messages.error(request, 'Username has already been taken')
            return redirect('register')

        if (password != password_confirm):
            messages.error(request, 'Passwords must be match the confirmation')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        messages.success(request, 'You are registered successfully. Please login here')
        return redirect('login')
        #auth.login(request, user)

    return render(request, 'accounts/register.html')

def dashboard(request):
    contacts = Contact.objects \
        .order_by('-contact_date') \
        .filter(user_id=request.user.id) 
    context = {
        'contacts': contacts
    }
    return render(request, 'accounts/dashboard.html', context)

def logout(request):
    auth.logout(request)
    return redirect('index')
