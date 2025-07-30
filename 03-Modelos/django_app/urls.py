from django.urls import path

from .views import PostListView # Importamos nuestra vista

urlpatterns = [
    path("", PostListView.as_view(), name = "PostList")  # Le asignamos una ruta a nuestra vista
]