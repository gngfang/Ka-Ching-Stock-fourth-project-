from django.shortcuts import render, redirect
# brining auth
from django.contrib.auth import authenticate, login, logout
# bringing form
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import RegisterForm
from .forms import EditUserForm
# bringing messages to send message
from django.contrib import messages


# import to fetch API
import requests
import json

# import models
from .models import Profile

# Create your views here.


def home(request):
    if request.method == 'POST':
        # grabbing the name value in our search form name as = ticker
        ticker = request.POST['ticker']

        # publisher key: pk_83d15d02cdd048a1b4aeddf3841592ef
        # import requests and pip3 install requests
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/"+ticker+"/quote?token=pk_83d15d02cdd048a1b4aeddf3841592ef")

    #  Python Try Except. The try block lets you test a block of code for errors.
    #      The except block lets you handle the error.
    #  The finally block lets you execute code,
    #  regardless of the result of the try- and except blocks.

        try:
            # import json, json is already inside no need to install
            api = json.loads(api_request.content)

        except Exception as e:
            api = "Error"

        context = {'api': api}
        return render(request, 'home.html', context)

    else:
        context = {'ticker': "Enter Symbol"}
        return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def follow_stock(request):
    return render(request, 'follow_stock.html')


def registration(request):
    """ Registration form and function. It save the form if is valid """
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # if User.objects.filter(email=email_register_form).exists():
            #     context={"Email already e"}
            register_form.save()
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(
                request, f'You successfully register {user.first_name}')
            return redirect('profile')

    else:
        register_form = RegisterForm()
    context = {'form': register_form}
    return render(request, 'registration.html', context)


def login_user(request):
    """ Login function if the request==post will do the following and will send a message depend on the success """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome Back {user.first_name}')
            return redirect('profile')

        else:

            messages.success(request, ('Error logging in. Please try again'))
            return redirect('login')
    else:

        return render(request, 'login.html')


def logout_user(request):
    """ Log out function once it successful will sent a message of You are logged out """
    logout(request)
    messages.success(request, ('You are logged out'))
    return redirect('home')


def profile(request):
    """ Profile view using user to request """
    user = request.user
    context = {'user': user}
    return render(request, 'profile.html', context)


def profile_edit(request, profile_id):
    # grabbing the profile id
    profile = Profile.objects.get(id=profile_id)

    if request.method == "POST":
        # giving the form
        user_form = EditUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
    else:
        user_form = EditUserForm(instance=request.user)

    context = {'form': user_form}
    return render(request, 'profile_edit.html', context)
