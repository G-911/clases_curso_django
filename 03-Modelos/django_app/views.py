from django.shortcuts import render  # Importación estándar (no usada directamente aquí)
from django.views.generic import (
    ListView,
)  # Importamos ListView, una "vista genérica" muy útil de Django.

# ListView está diseñada específicamente para mostrar listas de objetos de un modelo.
from .models import (
    Post,
)  # Importamos el modelo 'Post' desde el archivo models.py de nuestra misma aplicación.

# Este modelo es el que contiene los datos que queremos mostrar.

# Create your views here.


# Aquí definimos nuestra vista basada en clases.
# Heredamos de ListView, lo que nos da mucha funcionalidad "gratis" para mostrar listas.
class PostListView(ListView):
    # 'template_name' le dice a Django qué archivo HTML debe usar esta vista.
    # En este caso, usará 'home.html' para mostrar la lista de posts.
    template_name = "home.html"

    # 'model' le dice a ListView de qué modelo queremos obtener los objetos.
    # Aquí le indicamos que queremos obtener todos los objetos del modelo 'Post'.
    # ListView automáticamente tomará todos los 'Post' de la base de datos
    # y los enviará a 'home.html' bajo el nombre de 'object_list' o 'post_list' (por defecto).
    model = Post
