from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from custom_user.settings import AUTH_USER_MODEL
from myuser.models import MyUser
from myuser.forms import LoginForm, SignupForm
# Create your views here.
@login_required
def index_view(request):
    return render(request, "index.html", { "welcome": "Welcome!", "usermodel": AUTH_USER_MODEL})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("home_page"))
    
    form = LoginForm()
    return render(request, "generic_form.html", {"form" : form})


def signup_view(request):
    if request.method =="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(
                username=data.get("username"),
                password=data.get("password"),
                displayname=data.get("displayname"),
                age=data.get("age"),
                homepage=data.get('homepage')
                )
            if new_user:
                login(request, new_user)
                return HttpResponseRedirect(reverse("home_page"))
        
    form = SignupForm()
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home_page"))