from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def register_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}! Registration is successful!")
            return redirect('profile')
        else: 
            form = UserCreationForm()
            return render(request, 'authentication/register.html', {'form' : form})
        
def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}!")
                return redirect('profile')
            
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form' : form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out!")
    return redirect('login')

@login_required
def profile_view(request):
    return render(request, 'authentication/profile.html')


