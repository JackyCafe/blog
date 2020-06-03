from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from app1.forms import ExtendedUserCreationForm, UserProfileForm
from app1.models import UserProfile


def index(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = '尚未登入'

    context = {'username': username}
    return render(request,'html/index.html',context)


def register(request):
    form: ExtendedUserCreationForm
    user: User
    profile_form :UserProfileForm
    if request.method == 'POST':

        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            user_profile = profile_form.save(commit=False)
            user_profile.user = user
            user_profile.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            auth = authenticate(username=username, password=password)
            login(request, auth)
            return redirect(reverse('app1:index'))
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()
    context = {'form': form,'profile_form':profile_form}
    return render(request, 'html/register.html', context)


# def register(request):
    #
    # if request.method == 'POST':
    #     form = ExtendedUserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password1')
    #         auth = authenticate(username=username, password=password)
    #
    #         login(request, auth)
    #         return redirect('index')
    # else:
    #     form = ExtendedUserCreationForm()
    # context = {'form': form}
    # return render(request, 'html/register.html', context)
