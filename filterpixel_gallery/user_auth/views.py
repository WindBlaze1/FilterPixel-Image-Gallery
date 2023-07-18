from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from user_auth.forms import CreateUserForm
# Create your views here.

def signup_redirect(request):
    messages.error('You already have an account with the same Email. Login using that ID.')
    return redirect('login')

def index(request):
    return render(request, 'index.html')

def loginRequest(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect. Try Again.')

    return render(request, 'login.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        tnc = request.POST.get('tnc')
        print('here', type(tnc), tnc)
        if form.is_valid():
            if tnc=='on':
                form.save()
                messages.success(request, 'User created successfully!')
                return redirect('login')
            else:
                messages.error(request, 'You need to accept Terms and Conditions')
                return render(request, 'signup.html')
        else:
            print('errors',form.errors)
    else:
        form = CreateUserForm()

    
    return render(request, 'signup.html', {'form':form})

@login_required
def logoutRequest(request):
    logout(request)
    return redirect('index')