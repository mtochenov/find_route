from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import UserLoginForm, UserRegistrationForm
from .permissions import IsAuthenticated, AllowAny


def login_view(request):
    form = UserLoginForm(request.POST or None)
    _next = request.GET.get("next")
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        _next = _next or "/"
        return redirect(_next)
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/")
    # return render(request, "main/home.html")  # Так тоже работает выход на главную страницу


def registration_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)  # Будет создан экземпляр пользователя, но не сохранен со всеми данными
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            return render(request, "accounts/registration_finished.html", {"new_user": new_user})
        return render(request, "accounts/registration.html", {"form": form})
    else:
        form = UserRegistrationForm()
        return render(request, "accounts/registration.html", {"form": form})
