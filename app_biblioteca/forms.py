from cProfile import label
import email
from turtle import width
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import *

class Encargado_Form(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    codigo = forms.IntegerField()
    email = forms.CharField()

class Socio_Form(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    num_socio=forms.IntegerField()
    email=forms.EmailField()
    fecha_alta=forms.DateField()

class Libro_Form(forms.Form):
    titulo = forms.CharField(max_length=50)
    autor = forms.CharField(max_length=50)
    genero = forms.CharField(max_length=50)
    codigo =forms.IntegerField()


class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    last_name= forms. CharField()
    first_name= forms.CharField()
    class Meta:
        model=User
        fields= ['username', 'email', 'password1', 'password2','last_name','first_name']
        help_texts= {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email= forms.EmailField()
    last_name= forms.CharField()
    first_name=forms.CharField()
    
    class Meta:
        model=User
        fields= ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}

class PasswordChangeForm(UserCreationForm):
    email = forms.EmailField(label="em@il")
    password1 = forms.CharField(label = "password", widget = forms.PasswordInput)
    password2 =  forms.CharField(label = "password validador" , widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email","password1","password2"]
        help_texts = {k: "" for k in fields}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')
        
        widget = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'autor': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        
        }   

class EditarForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo','body')
        
        widget = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'autor': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        
        }   