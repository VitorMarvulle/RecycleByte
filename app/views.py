from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

def app(request):
    template = loader.get_template("home.html")

    return HttpResponse(template.render())

def home_view(request):
    return render(request, 'home.html')

def profile_view(request):
    return render(request, 'profile.html')