from django.shortcuts import render  # Importación estándar (no usada directamente aquí)
from django.views.generic import (
    TemplateView,
)  # Importamos TemplateView para crear una vista que renderiza una plantilla HTML

# Creamos aquí las vistas de la aplicación


class HomePageView(TemplateView):
    # Esta vista hereda de TemplateView, lo que significa que su único propósito es mostrar una plantilla HTML estática.

    template_name = "home.html"
    # Especificamos el nombre del archivo de plantilla que se va a renderizar.
    # Django buscará este archivo dentro del directorio configurado en TEMPLATES['DIRS'] o dentro de una app si APP_DIRS=True.

    # No necesitamos escribir un método 'get' manual si solo vamos a renderizar contenido estático.
    # Si quisiéramos pasar datos adicionales al contexto, podríamos sobreescribir el método get_context_data().
