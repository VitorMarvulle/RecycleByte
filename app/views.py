from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UsuarioForm
from .mongo import mongoDB

def app(request):
    template = loader.get_template("home.html")

    return HttpResponse(template.render())

def home_view(request):
    return render(request, 'home.html')

def profile_view(request):
    return render(request, 'profile.html')

def cadastrar_usuario(request):
    db = mongoDB()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']


            db.usuarios.insert_one({
                'nome':nome,
                'email':email,
                'senha':senha
            })

            return redirect('home')
    else:
        form = UsuarioForm()
    
    return render(request,'cadastro.html',{'form':form})