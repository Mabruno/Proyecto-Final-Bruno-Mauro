from django.shortcuts import render
from WebMDev_app.models import Producto, Consulta, Compra
from WebMDev_app.forms import Consultaform, UserRegisterForm, Compraform, UpdateForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect



def inicio(request):
    return render(request, 'inicio.html')

def enobra(request):
    return render(request, 'enobra.html')


#--->MODULO DE PRODUCTOS<---

class Productoslist(ListView):

    model = Producto
    template_name = 'productos.html'


class Productosdetail(DetailView):

    model = Producto
    template_name = "productos_detail.html"
    context_object_name = "producto"
    slug_field = "slug"


class Productosadmin(ListView):

    model = Producto
    template_name = "productos_admin.html"

class Productoscreacion(CreateView):

    model = Producto
    success_url = reverse_lazy('productos_admin')
    fields = ['nombre', 'descripcion', 'precio', 'valoracion', 'idnumber', 'imagen', 'slug']

class Productosupdate(UpdateView):

    model = Producto
    success_url = reverse_lazy('productos_admin')
    template_name = 'productos_update.html'
    form_class = UpdateForm
    slug_field = "slug"

    def form_valid(self, form):
        # Save the changes made by the user
        print("form_valid method called!")
        self.object = form.save()
        return super().form_valid(form)
        #fields = ['nombre', 'descripcion', 'precio', 'valoracion', 'idnumber', 'imagen', 'slug']

class Productosdelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos_admin.html')
    template_name = 'productos_delete.html'



class Productosofer(ListView):

    model = Producto
    template_name = 'ofertas.html'



#--->MODULO DE USUARIOS<---
#---->LOGIN - REGISTRO DE  USUARIO<-----


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "login_failed.html", {"mensaje": "Datos incorrectos"})

        else:

            return render(request, "login_failed.html", {"mensaje": "Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def register(request):
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "inicio.html", {"mensaje": "Usuario Creado :)"})

    else:
        form = UserRegisterForm(request.POST)

    return render(request, "registro.html", {"form": form})


#--->MODULO DE CONTACTO<---

def contacto(request):

    if request.method == 'POST':
        formulario_consulta = Consultaform(request.POST)

        if formulario_consulta.is_valid():
            informacion = formulario_consulta.cleaned_data
            consulta = Consulta(nombre=informacion['nombre_form'], email=informacion['email'],
                                  tema=informacion['tema'], mensaje=informacion['mensaje'])
            consulta.save()

            return render(request, 'contacto.html')

    else:
        formulario_consulta = Consultaform()

    return render(request, 'contacto.html', {'formulario_consulta': formulario_consulta})




#--->MODULO DE COMPRA---

@login_required()
def compra(request):

    if request.method == 'POST':
        formulario_compra = Compraform(request.POST)

        if formulario_compra.is_valid():

            informacion = formulario_compra.cleaned_data

            compra = Compra(username=informacion['username'], pago=informacion['pago'],
                                  envio=informacion['envio'], mensaje=informacion['mensaje'])
            compra.save()

            return render(request, "inicio.html", {"mensaje": f"Su mensaje fue enviado"})

        else:
            print(formulario_compra.errors)

    else:

        formulario_compra = Compraform()


    return render(request, 'compra.html', {'formulario_compra': formulario_compra})


def nosotros(request):
    return render(request, 'nosotros.html')


"""def productosupdate(request, nombre):

    # Recibe el nombre del profesor que vamos a modificar
    producto = Producto.objects.get(nombre=nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        formulario_update = UpdateForm(request.POST)

        print(formulario_update)

        if formulario_update.is_valid:  # Si pasó la validación de Django

            informacion = formulario_update.cleaned_data

            producto.nombre = informacion['nombre']
            producto.descripcion = informacion['descripcion']
            producto.valoracion = informacion['valoracion']
            producto.precio = informacion['precio']
            producto.tamaño = informacion['tamaño']
            producto.idnumber = informacion['idnumber']
            producto.imagen= informacion['imagen']

            producto.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "productos_admin.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        formulario_update = UpdateForm(initial={'nombre': producto.nombre, 'descripcion': producto.descripcion,
                                                   'valoracion': producto.valoracion, 'precio': producto.precio, 'tamaño': producto.tamaño, 'idnumber': producto.idnumber, 'imagen': producto.imagen})

    # Voy al html que me permite editar
    return render(request, "productos_update.html", {"formulario_update": formulario_update, "nombre": nombre})"""
