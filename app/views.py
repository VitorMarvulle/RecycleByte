from django.shortcuts import render, redirect
from .forms import UsuarioForm,UsuarioLoginForm, UsuarioEditForm
from .mongo import mongoDB
import folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from django.contrib.auth.hashers import check_password,make_password
from django.contrib import messages
from datetime import timedelta
import pymongo
import pymongo.errors
from django.contrib.auth import logout
from django.http import JsonResponse

def app(request):
    return render(request, "home.html",{'messages': messages.get_messages(request)})

def home_view(request):
    return render(request, 'home.html')

def profile_view(request):
    

    context={
        'emailname':email,
        'username':nome
    }

    return render(request, 'profile.html',context)
        
def apoie_view(request):
    return render(request, 'apoie.html')

def reciclar_view(request):
    return render(request, 'reciclar.html')

def noticias_view(request):
    return render(request, 'noticias.html')

def campanhas_view(request):
    return render(request, 'campanhas.html')

def eventos_view(request):
    return render(request, 'eventos.html')

def cadastrar_usuario(request):
    db = mongoDB()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            senha_rash = make_password(senha)

            db.usuarios.insert_one({
                'nome':nome,
                'email':email,
                'senha':senha_rash,
                'cpf':None,
                'endereco':None,
                'nivel':0,
                'xp':0,
                'recycoins':0,
                'rc_papel':0,
                'rc_plastico':0,
                'rc_metal':0,
                'rc_vidro':0,
                'img_perfil':None
            })
            messages.success(request,"Usuario cadastrado com sucesso!")
            return redirect('home')
    else:
        form = UsuarioForm()
    return render(request,'cadastro.html',{'form':form})


def get_coordinates(address):
    """Obtém as coordenadas a partir de um endereço usando Geopy."""
    geolocator = Nominatim(user_agent="meu_app")  # Substitua "meu_app" pelo nome do seu aplicativo
    try:
        location = geolocator.geocode(address)
        if location:
            return (location.latitude, location.longitude)
        else:
            return None
    except GeocoderTimedOut:
        return get_coordinates(address)  # Tenta novamente em caso de timeout

def mapa_view(request):
    lat = float(request.GET.get('lat', -23.5505))  # Pega a latitude, default é São Paulo
    lng = float(request.GET.get('lng', -46.6333))  # Pega a longitude, default é São Paulo
    address = request.GET.get('address', None)  # Pega o endereço do request, se disponível

    # Se um endereço for fornecido, tenta obter as coordenadas
    if address:
        coords = get_coordinates(address)
        if coords:
            lat, lng = coords
        else:
            # Se não conseguiu obter coordenadas, usa os padrões
            lat, lng = -24.0055, -46.3903    

    # Cria o mapa baseado na localização do usuário
    m = folium.Map(location=[lat, lng], zoom_start=16)

    folium.Marker(
        location=[lat,lng],
        popup='Você esta aqui',
        icon=folium.Icon(color='red')
    ).add_to(m)

    # Adiciona marcadores de locais de reciclagem próximos (você pode obter isso de um banco de dados, por exemplo)
    pontos_reciclagem = [
        {"nome": "Mundo Clean Reciclagem", "lat": -24.00440198499218, "lng": -46.43729567093028},
        {"nome": "Bola Reciclagem", "lat": -24.012240611117054, "lng": -46.45292223052698},
        {"nome": "Grupo Paco Reciclagem", "lat": -24.012817485175056, "lng": -46.457613586874714},
        {"nome": "Alboreda Comercio de Materiais Recicláveis", "lat": -24.01431734561621, "lng": -46.454834860422594},
        {"nome": "Gloria Reciclagem", "lat": -24.00775380276044, "lng": -46.43647518380789},
        {"nome": "Mundo Clean Reciclagem", "lat": -24.004638529478466, "lng": -46.43732323668615},
        {"nome": "Joao do Oleo", "lat": -24.006962629390824, "lng": -46.44075153555564},
        {"nome": "Associação dos Catadores de Materiais Recicláveis PG Acamar", "lat": -24.00712745757742, "lng": -46.44722921605117},
        {"nome": "Ecoponto Vila Sonia", "lat": -24.003946236282733, "lng": -46.44773443904246},
        {"nome": "Cooperlix", "lat": -24.019620613069044, "lng": -46.46691136987444},
        {"nome": "Comércio de Reciclagem Ph", "lat": -24.01485303286168, "lng": -46.48772854056273},
        {"nome": "Chico Metais", "lat": -24.015157941538934, "lng": -46.489579630015534},
        {"nome": "Comércio de Reciclagem", "lat": -24.018151551986396, "lng": -46.491885905623064},
        {"nome": "Sucatas Bacteria", "lat": -24.03082601054962, "lng": -46.51091035254699},
        {"nome": "Ponto de Reciclagem Metal Nobre", "lat": -24.034431966207585, "lng": -46.512798627557},
        {"nome": "Reciclagem Planalto", "lat": -24.02788629791338, "lng": -46.50730546389153},
        {"nome": "Solange Engem", "lat": -24.02326101391049, "lng": -46.50992329970086},
        {"nome": "Ecoponto Antartica", "lat": -24.005784548127675, "lng": -46.457340895478666},
        {"nome": "Ecoponto Vila Sonia", "lat": -24.003863569413323, "lng": -46.44781368974637},
        {"nome": "Biolitoral - Reciclagem de Óleo Vegetal", "lat": -23.99723793287816, "lng": -46.42051953018739},
    ]
    for local in pontos_reciclagem:
        folium.Marker(
            location=[local['lat'], local['lng']],
            popup=local['nome'],
            icon=folium.Icon(color='green')
        ).add_to(m)

    # Salva o mapa em HTML
    mapa_html = m._repr_html_()
    return render(request, 'mapa.html', {'mapa': mapa_html})

def fazerLogin(request):
    if request.method == "POST":
        form = UsuarioLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
 
            try:
                db = mongoDB()
                usuario = db.usuarios.find_one({'email': email})
 
                if usuario and check_password(senha, usuario['senha']):
                    request.session['email'] = email
                    request.session['nome'] = usuario['nome']
                    return redirect('profile_default')
                else:
                    return redirect('home')
 
            except pymongo.errors.PyMongoError as e:
                return JsonResponse({'success': False, 'message': f'Ocorreu um erro ao acessar o banco de dados: {e}'})
 
    return redirect('home')

def userLogout(request):
	logout(request)
	messages.success(request, 'A sessao foi encerrada!')
	return redirect('home')

def profile(request, conteudo='resumo'):
    if "email" not in request.session:
        messages.error(request,"Sessao expirada, entre novamente")
        return redirect("login")
    
    db = mongoDB() 
    collection = db['usuarios']  

    email = request.session.get('email')

    nome = None
    nivel = None
    xp = None

    if email:
        usuario = collection.find_one({'email': email})
        if usuario:
            nome = usuario.get('nome')
            nivel = usuario.get('nivel', 1)
            xp = usuario.get('xp', 0)

    context = {
        'conteudo': conteudo,
        'username': nome,
        'nivel': nivel,
        'xp': xp,
    }
    return render(request, 'profile.html', context)

def increase_xp(request):
    db = mongoDB() 
    collection = db['usuarios']

    email = request.session.get('email')
    if not email:
        return redirect('profile')

    usuario = collection.find_one({'email': email})
    if usuario:
        xp_atual = usuario.get('xp', 0)
        nivel_atual = usuario.get('nivel', 1)

        novo_xp = xp_atual + 20

        if novo_xp >= 100:
            nivel_atual += novo_xp // 100
            novo_xp = novo_xp % 100

        # Atualiza o banco de dados
        collection.update_one(
            {'email': email},
            {'$set': {'xp': novo_xp, 'nivel': nivel_atual}}
        )
    return redirect('profile_default')

def profile_edit(request):
    db = mongoDB()  # Supondo que você tenha uma conexão com MongoDB configurada.
    
    # Suponha que você queira carregar as informações do usuário logado
    usuario = db.usuarios.find_one({"email": request.user.email})  # Ajuste conforme seu banco de dados

    # Definir o nível e experiência para o template
    nivel = usuario.get('nivel', 'Iniciante')  # Exemplo: Defina um valor padrão
    experiencia_xp = usuario.get('experiencia_xp', 0)

    if request.method == 'POST':
        form = UsuarioEditForm(request.POST, request.FILES)
        
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            cpf = form.cleaned_data['cpf']
            endereco = form.cleaned_data['endereco']

            # Processamento de senha
            if senha:  # Só criptografa a senha se o usuário forneceu uma nova senha
                senha_rash = make_password(senha)
            else:
                senha_rash = usuario['senha']  # Mantém a senha atual, caso não tenha sido alterada

            # Verifica se a imagem foi alterada
            
            # Atualiza os dados do usuário no MongoDB
            db.usuarios.update_one(
                {"email": email},  # Filtra pelo e-mail ou outro campo único
                {"$set": {
                    'nome': nome,
                    'email': email,
                    'senha': senha_rash,
                    'cpf': cpf,
                    'endereco': endereco,
                }}
            )

            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('profile')  # Ajuste a URL de redirecionamento

    else:
        form = UsuarioEditForm(initial={
            'nome': usuario.get('nome', ''),
            'email': usuario.get('email', ''),
            'cpf': usuario.get('cpf', ''),
            'endereco': usuario.get('endereco', ''),
        })

    return render(request, 'profile_edit.html', {
        'form': form,
        'nivel': nivel,
        'experiencia_xp': experiencia_xp,
    })

def resumo_view(request):
    db = mongoDB()
    collection = db['feitos']
    dados = list(collection.find())
    return render(request, 'profile_default', {'dados': dados})