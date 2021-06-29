from django.shortcuts import render


def home(request):
    data = {
        "title": "Cities",
    }

    return render(request, "main/home.html", data)
