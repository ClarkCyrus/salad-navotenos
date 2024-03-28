from django.shortcuts import render, redirect, get_object_or_404
from salad.models import Salad
from django.http import HttpResponse
from customer.models import Customer
from django.contrib.auth import authenticate, login, logout
from main.backends import CustomerAuthentication

def home(request):
    return render(request, 'home.html')

def room(request):
    salads=Salad.objects.all()
    return render(request, 'room.html', {'salads': salads})

def salad_detail(request, pk):
    salad = get_object_or_404(Salad, pk=pk)
    return render(request, 'salad_detail.html', {'salad': salad})

def signin(request):
    if request.method == 'POST':
        username_contact_number = request.POST.get('inputUsernameContactNumber')
        password = request.POST.get('inputPassword')

        user = CustomerAuthentication().authenticate(request, username=username_contact_number, password=password)

        if user is not None:
            # If authentication succeeds, log in the user
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else:
            # If authentication fails, display an error message
            return render(request, 'signin.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST': # POST means sending data to the server

        # Get neccessary info with name attribute in form of signup.html
        username = request.POST.get('inputUsername')
        contact_number = request.POST.get('inputContactNumber')
        password = request.POST.get('inputPassword')
        confirm_password = request.POST.get('confirmInputPassword')

        # Validate all fields for emptiness
        if not all([username, contact_number, password, confirm_password]):
            return render(request, 'signup.html', {'error_message': 'All fields are required'})

        # Mismatch password
        if password != confirm_password:
            return render(request, 'signup.html', {'error_message': 'Passwords do not match'})

        # Reject username if already exists in the database
        if Customer.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error_message': 'Username already taken'})

        # Mismatch password
        if password != confirm_password:
            return render(request, 'signup.html', {'error_message' : 'password failed to match'})

        # Reject username if already exist in database
        if Customer.objects.filter(username = username).exists():
            return render(request, 'signup.html', {'error_message' : 'username already taken'})

        # Put in database
        user = Customer.objects.create_user(username=username, contact_number=contact_number, password=password)
        user.save()
        
        # Proceed to sign in page
        return redirect('home')

    else:
        # Called first when signup/ is entererd
        return render(request, 'signup.html')
    

def signout(request):
    logout(request)
    return redirect('home')
