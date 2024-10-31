from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.app, name="home"),
    path('profile/', views.profile_view, name='profile'),
    path('cadastro/',views.cadastrar_usuario, name='cadastro'),
    path('mapa/', views.mapa_view, name='mapa'),
    path('reciclar/', views.reciclar_view, name='reciclar'),
    path('login/', views.fazerLogin, name='fazerLogin'),
    path('logout/', views.userLogout, name='logout')
]