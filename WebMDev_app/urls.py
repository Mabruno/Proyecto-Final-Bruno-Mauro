from WebMDev_app import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('enobra/', views.enobra, name='enobra'),
    path('contacto/', views.contacto, name='contacto'),
    path('compra/', views.compra, name='compra'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('ofertas/', views.Productosofer.as_view(), name='ofertas'),
    path('productos/', views.Productoslist.as_view(), name='productos'),
    path('login/', views.login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('templates/<slug:slug>/', views.Productosdetail.as_view(), name='productos'),
    path('admin/productos/<slug:slug>/', views.Productosupdate.as_view(), name='update'),
    path('admin/productos/delete/<slug:slug>', views.Productosdelete.as_view(), name='delete'),
    path('productos/admin/', views.Productosadmin.as_view(), name='admin'),
    #path('updateproductos/<nombre>/', views.productosupdate, name='updateproducto'),

]