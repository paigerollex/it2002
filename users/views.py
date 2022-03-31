from email import message
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

# Create your views here.
def signup(request):
    form = UserRegistrationForm(request.POST or None)
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print("VALID")
            form.save()
            student_id = form.cleaned_data['username']
            messages.success(request, f'Account successfully created for {student_id}!')
            return redirect('signin')
        
        else:
            print("INVALID")
            messages.info(request, 'invalid registration details')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or password is incorrect")
         
    return render(request, 'login.html', {})


def signout(request):
    logout(request)
    messages.success(request, ("You have successfully logged out!"))
    return render(request, 'logout.html', {})


def home(request):
    return render(request, 'home.html', {})