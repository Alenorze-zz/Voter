from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, its last chance...</h2>")
