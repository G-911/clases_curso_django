"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .view import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home')
    """
    Esta ruta vacía ('') representa la raíz del sitio web: http://localhost:8000/
    Cuando un usuario accede a esa URL sin ninguna subruta adicional,
    Django ejecuta la vista HomeView para mostrar la página principal.
    El método as_view() convierte la clase HomeView en una vista funcional que Django puede usar.
    Además, el parámetro name='home' permite referirse a esta URL desde plantillas con {% url 'home' %}
    """
]

"""
Configuración de URLs para el proyecto django_project.

La lista `urlpatterns` enruta las solicitudes HTTP a las vistas correspondientes.
Más información en: https://docs.djangoproject.com/en/5.2/topics/http/urls/

📝 DESCRIPCIÓN DE LAS RUTAS

- path(): función utilizada para definir rutas en Django.
- HomeView: clase que representa la vista que será renderizada.
- .as_view(): convierte la clase en una vista que Django puede procesar.
- name='home': nombre de la ruta, útil para referenciarla desde los templates (por ejemplo, con {% url 'home' %}).
"""