from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Producto(models.Model):
    nombre = models.CharField(max_length=40, default='')
    descripcion = models.CharField(max_length=100)
    idnumber = models.IntegerField()
    tamaño = models.FloatField(default=0.0)
    precio = models.FloatField(default=0.0)
    valoracion = models.FloatField(max_length=4, default=0.0)
    imagen = models.ImageField(default=True, upload_to='static/WebMDev_app/assets/img')
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('productos', kwargs={'slug': self.slug})

    def __str__(self):
        return f"Nombre: {self.nombre} - Descripcion {self.descripcion} - IDnum {self.idnumber} - Precio {self.precio} - Valoracion {self.valoracion}"


class Usuario(models.Model):
    idusuario = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    contraseña = models.CharField(max_length=20, default='')

    def __str__(self):
        return f"IDusu: {self.idusuario} - Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"


class User(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField()
    first_name = models.CharField(default='', max_length=100)
    last_name = models.CharField(default='', max_length=100)
    password1 = models.CharField(max_length=40)
    password2 = models.CharField(max_length=20, default='')


    def __str__(self):
        return f"IDusu: {self.idusuario} - Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"

class Compra(models.Model):
    username = models.CharField(default='', max_length=40)
    pago = models.CharField(max_length=40)
    envio = models.CharField(max_length=40)
    mensaje = models.CharField(default=None, max_length=100)

    def __str__(self):
        return f"Usuario {self.username} - Pago {self.pago} -   Envio {self.envio} - Mensaje {self.mensaje}"

class Consulta(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    tema = models.CharField(max_length=40)
    mensaje = models.CharField(default='', max_length=200)

    def __str__(self):
        return f"Nombre: {self.nombre} - Email {self.email} -   Tema {self.tema} - Mensaje {self.mensaje}"

class UserCreationForm(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField()
    password1 = models.CharField(max_length=40)
    password2 = models.CharField(max_length=20, default='')