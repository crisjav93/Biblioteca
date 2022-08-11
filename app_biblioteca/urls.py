from django.urls import path,include
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin



urlpatterns = [

    path('', inicio, name='inicio'),
    path('encargados/', encargados, name='encargados'),
    path('socios/',socios, name='socios'),
    path('libros/',libros,name='libros'),
    path('ingreso_encargados/',ingreso_encargados, name='ingreso_encargados'),
    path('ingreso_socios/', ingreso_socios, name = 'ingreso_socios'),
    path('ingreso_libros/', ingreso_libros, name='ingreso_libros'),
    path('buscar_libro/', busqueda_libro, name = 'buscar_libro'),
    path('resultado_libro/', buscar_libro, name='resultado_libro'),
    path('buscar_socio/', busqueda_socio, name = 'buscar_socio'),
    path('resultado_socio/', buscar_socio, name='resultado_socio'),
    path('buscar_encargado/', busqueda_encargado, name = 'buscar_encargado'),
    path('resultado_encargado/', buscar_encargado, name='resultado_encargado'),
    path('leer_encargados/',leer_encargados, name='leer_encargados'),
    path('leer_libros/', leer_libros, name='leer_libros'),
    path('leer_socios/', leer_socios, name = 'leer_socios'),
    path('eliminar_encargado/<codigo_encargado>', eliminar_encargado, name='eliminar_encargado'),
    path('eliminar_libro/<codigo_libro>', eliminar_libro, name='eliminar_libro'),
    path('eliminar_socio/<num_soc>', eliminar_socio, name='eliminar_socio'),
    path('editar_encargado/<codigo_encargado>', editar_encargado, name='editar_encargado'),
    path('editar_socio/<num_soc>', editar_socio, name='editar_socio'),
    path('editar_libro/<codigo_libro>', editar_libro, name='editar_libro'),
    path('social/', HomeView.as_view(), name='social' ),
    path('article_detail/<int:pk>',ArticleDetailView.as_view(), name='article_detail' ),#pk=private key, asigna un codigo único al articulo en este caso
    path('agregar_post/', agregar_post.as_view(),name = 'agregar_post'),
    path('article_detail/editar_post/<int:pk>', editar_post.as_view(), name = 'editar_post'),
    path('article_detail/<int:pk>/eliminar', eliminar_post.as_view(), name = 'eliminar_post'),

    
    #LOGIN----------------------------------------------------------------
    
    path('login/', login_request, name='login'),
    #REGISTRARSE----------------------------------------------------------------
    path('register/', register, name='register'),
    #LOGOUT-------------------------------------------------------------------
    path('logout/', LogoutView.as_view(template_name='app_biblioteca/logout.html'), name='logout'),
    path('inicio/', inicio, name='inicio'),

    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('editar_pass/', editar_pass, name='editar_pass'),

   


]
