from django.urls import path  # Importamos la función `path` para definir rutas URL
from .views import (
    HomePageView,
)  # Importamos la vista HomePageView que será renderizada cuando se acceda a la ruta raíz

# Lista de rutas que esta aplicación manejará.
urlpatterns = [
    path("", HomePageView.as_view(), name="home")
    # Esta ruta vacía ('') representa la URL raíz de esta aplicación.
    # Cuando un usuario accede directamente a '/', Django llamará a la vista HomePageView.
    # `.as_view()` transforma la clase `HomePageView` en una vista que Django puede ejecutar.
    # Es útil cuando estás trabajando con vistas basadas en clases (Class-Based Views).
    # `name="home"` asigna un nombre simbólico a esta ruta.
    # Esto permite referenciarla fácilmente en plantillas usando: {% url 'home' %}
]
