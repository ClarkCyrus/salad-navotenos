from django.shortcuts import render, redirect, get_object_or_404
from salad.models import Salad
from django.http import HttpResponse
from users.models import Salad_Customer, Salad_Employee, Crochet_Customer, Crochet_Employee
from django.contrib.auth import authenticate, login, logout
from main.backends import CustomerAuthentication

def salad_home(request):
    return render(request, 'salad_home.html')

def crochet_home(request):
    return render(request, 'crochet_home.html')

def salad_room(request):
    return render(request, 'salad_room.html')

def crochet_room(request):
    return render(request, 'crochet_room.html')

def salad_signin(request):
    if request.method == 'POST':
        username_contact_number = request.POST.get('inputUsernameContactNumber')
        password = request.POST.get('inputPassword')

        user = CustomerAuthentication().authenticate_salad_customer(request, username=username_contact_number, password=password)

        if user is not None:
            # If authentication succeeds, log in the user
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('salad_home')
        else:
            # If authentication fails, display an error message
            return render(request, 'salad_customer_signin.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'salad_customer_signin.html')
    
def crochet_signin(request):
    if request.method == 'POST':
        username_contact_number = request.POST.get('inputUsernameContactNumber')
        password = request.POST.get('inputPassword')

        user = CustomerAuthentication().authenticate_crochet_customer(request, username=username_contact_number, password=password)

        if user is not None:
            # If authentication succeeds, log in the user
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('crochet_home')
        else:
            # If authentication fails, display an error message
            return render(request, 'crochet_customer_signin.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'crochet_customer_signin.html')


def salad_signup(request):
    if request.method == 'POST': # POST means sending data to the server

        # Get neccessary info with name attribute in form of signup.html
        username = request.POST.get('inputUsername')
        contact_number = request.POST.get('inputContactNumber')
        password = request.POST.get('inputPassword')
        confirm_password = request.POST.get('confirmInputPassword')

        # Validate all fields for emptiness
        if not all([username, contact_number, password, confirm_password]):
            return render(request, 'salad_customer_signup.html', {'error_message': 'All fields are required'})

        # Mismatch password
        if password != confirm_password:
            return render(request, 'salad_customer_signup.html', {'error_message': 'Passwords do not match'})

        # Reject username if already exists in the database
        if Salad_Customer.objects.filter(username=username).exists():
            return render(request, 'salad_customer_signup.html', {'error_message': 'Username already taken'})

        # Mismatch password
        if password != confirm_password:
            return render(request, 'salad_customer_signup.html', {'error_message' : 'password failed to match'})

        # Reject username if already exist in database
        if Salad_Customer.objects.filter(username = username).exists():
            return render(request, 'salad_customer_signup.html', {'error_message' : 'username already taken'})

        # Put in database
        user = Salad_Customer.objects.create_user(username=username, contact_number=contact_number, password=password)
        user.save()
        
        # Proceed to sign in page
        return redirect('salad_home')

    else:
        # Called first when signup/ is entererd
        return render(request, 'salad_customer_signup.html')
    
def crochet_signup(request):
    if request.method == 'POST': # POST means sending data to the server

        # Get neccessary info with name attribute in form of signup.html
        username = request.POST.get('inputUsername')
        contact_number = request.POST.get('inputContactNumber')
        password = request.POST.get('inputPassword')
        confirm_password = request.POST.get('confirmInputPassword')

        # Validate all fields for emptiness
        if not all([username, contact_number, password, confirm_password]):
            return render(request, 'crochet_customer_signup.html', {'error_message': 'All fields are required'})

        # Mismatch password
        if password != confirm_password:
            return render(request, 'crochet_customer_signup.html', {'error_message': 'Passwords do not match'})

        # Reject username if already exists in the database
        if Crochet_Customer.objects.filter(username=username).exists():
            return render(request, 'crochet_customer_signup.html', {'error_message': 'Username already taken'})

        # Mismatch password
        if password != confirm_password:
            return render(request, 'crochet_customer_signup.html', {'error_message' : 'password failed to match'})

        # Reject username if already exist in database
        if Crochet_Customer.objects.filter(username = username).exists():
            return render(request, 'crochet_customer_signup.html', {'error_message' : 'username already taken'})

        # Put in database
        user = Crochet_Customer.objects.create_user(username=username, contact_number=contact_number, password=password)
        user.save()
        
        # Proceed to sign in page
        return redirect('crochet_home')

    else:
        # Called first when signup/ is entererd
        return render(request, 'crochet_customer_signup.html')
    
def salad_employee_signin(request):
    if request.method == 'POST':
        username = request.POST.get('inputUsername')
        password = request.POST.get('inputPassword')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If authentication succeeds, log in the user
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('salad_home')
        else:
            # If authentication fails, display an error message
            return render(request, 'salad_employee_signin.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'salad_employee_signin.html')
    
def crochet_employee_signin(request):
    if request.method == 'POST':
        username = request.POST.get('inputUsername')
        password = request.POST.get('inputPassword')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If authentication succeeds, log in the user
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('crochet_home')
        else:
            # If authentication fails, display an error message
            return render(request, 'crochet_employee_signin.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'crochet_employee_signin.html')
    
def salad_employee_signup(request):
    if request.method == 'POST': # POST means sending data to the server

        # Get neccessary info with name attribute in form of signup.html
        username = request.POST.get('inputUsername')
        password = request.POST.get('inputPassword')
        confirm_password = request.POST.get('confirmInputPassword')

        # Validate all fields for emptiness
        if not all([username, password, confirm_password]):
            return render(request, 'salad_employee_signup.html', {'error_message': 'All fields are required'})

        # Mismatch password
        if password != confirm_password:
            return render(request, 'salad_employee_signup.html', {'error_message': 'Passwords do not match'})

        # Reject username if already exists in the database
        if Salad_Employee.objects.filter(username=username).exists():
            return render(request, 'salad_employee_signup.html', {'error_message': 'Username already taken'})

        # Mismatch password
        if password != confirm_password:
            return render(request, 'salad_employee_signup.html', {'error_message' : 'password failed to match'})

        # Reject username if already exist in database
        if Salad_Employee.objects.filter(username = username).exists():
            return render(request, 'salad_employee_signup.html', {'error_message' : 'username already taken'})

        # Put in database
        user = Salad_Employee.objects.create_user(username=username, password=password)
        user.save()
        
        # Proceed to sign in page
        return redirect('salad_home')
    
    else:
        # Called first when signup/ is entererd
        return render(request, 'salad_employee_signup.html')
    
def crochet_employee_signup(request):
    if request.method == 'POST': # POST means sending data to the server

        # Get neccessary info with name attribute in form of signup.html
        username = request.POST.get('inputUsername')
        password = request.POST.get('inputPassword')
        confirm_password = request.POST.get('confirmInputPassword')

        # Validate all fields for emptiness
        if not all([username, password, confirm_password]):
            return render(request, 'crochet_employee_signup.html', {'error_message': 'All fields are required'})

        # Mismatch password
        if password != confirm_password:
            return render(request, 'crochet_employee_signup.html', {'error_message': 'Passwords do not match'})

        # Reject username if already exists in the database
        if Crochet_Employee.objects.filter(username=username).exists():
            return render(request, 'crochet_employee_signup.html', {'error_message': 'Username already taken'})

        # Mismatch password
        if password != confirm_password:
            return render(request, 'crochet_employee_signup.html', {'error_message' : 'password failed to match'})

        # Reject username if already exist in database
        if Crochet_Employee.objects.filter(username = username).exists():
            return render(request, 'crochet_employee_signup.html', {'error_message' : 'username already taken'})

        # Put in database
        user = Crochet_Employee.objects.create_user(username=username, password=password)
        user.save()
        
        # Proceed to sign in page
        return redirect('crochet_home')
    
    else:
        # Called first when signup/ is entererd
        return render(request, 'crochet_employee_signup.html')

def salad_signout(request):
    logout(request)
    return redirect('salad_home')

def crochet_signout(request):
    logout(request)
    return redirect('crochet_home')
