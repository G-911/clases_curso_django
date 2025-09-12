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
from django.urls import (
    path,
    include,
)  # `include` permite agregar rutas definidas en otras apps

urlpatterns = [
    path("admin/", admin.site.urls),
    # Aquí usamos `include()` para enlazar las rutas definidas en django_app/urls.py.
    # Esto permite mantener el enrutamiento modular y organizado por aplicación.
    path(
        "", include("django_app.urls")
    ),  # La raíz del sitio web delega sus URLs a la app django_app
]

"""
    🧭 Esta es una ruta *vacía*, representada por las comillas: ''.
    Significa que cuando el usuario accede directamente a la raíz del sitio web (por ejemplo, 'http://localhost:8000/'),
    Django mostrara la vista asignada a esta ruta

    ⚠️ Es importante entender que '' no es un nombre de carpeta, sino la parte inicial de la URL.
    Si en lugar de '' pusieras 'blog/', entonces Django buscaría las vistas en 'django_app.urls'
    solo si el usuario accede a 'http://localhost:8000/blog/'.
"""
