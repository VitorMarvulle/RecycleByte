from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.app, name="home"),
    path('profile/', views.profile_view, name='profile'), 

]