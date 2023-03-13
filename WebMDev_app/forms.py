from django import forms
#from .views import
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Consultaform(forms.Form):
    nombre_form = forms.CharField(max_length=40)
    email = forms.EmailField()
    tema = forms.CharField(max_length=40)
    mensaje = forms.CharField(max_length=200)

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=False)
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)


    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class Compraform(forms.Form):
    username = forms.CharField(max_length=40)
    pago = forms.CharField()
    envio = forms.CharField(max_length=40)
    mensaje = forms.CharField(max_length=200)


class UpdateForm(UserCreationForm):
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    descripcion = forms.CharField(label='Descripcion', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=False)
    idnumber = forms.IntegerField(label="IDnumber", widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    tamaño = forms.CharField(label='Tamaño', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    precio = forms.IntegerField(label='Precio', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    valoracion = forms.CharField(label='Valorcion', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=False)
    imagen = forms.ImageField(label="Imagen", widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)
    slug = forms.CharField(label='Slug', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
