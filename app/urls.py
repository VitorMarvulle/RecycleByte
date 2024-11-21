from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.app, name="home"),
    path('profile/', views.profile_view, name='profile'),
    path('cadastro/',views.cadastrar_usuario, name='cadastro'),
    path('mapa/', views.mapa_view, name='mapa'),
    path('reciclar/', views.reciclar_view, name='reciclar'),
    path('noticias/', views.noticias_view, name='noticias'),
    path('campanhas/', views.campanhas_view, name='campanhas'),
    path('eventos/', views.eventos_view, name='eventos'),

    path('login/', views.fazerLogin, name='fazerLogin'),
    path('logout/', views.userLogout, name='logout'),
    path('apoie/', views.apoie_view, name='apoie'),
    path('increase_xp/', views.increase_xp, name='increase_xp'),

    path('profile/<str:conteudo>/', views.profile, name='profile'),
    path('profile/resumo', views.profile, name='profile_default')
]