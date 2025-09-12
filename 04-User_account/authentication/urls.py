from django.contrib import admin
from django.urls import path, include
from .views import SignUpView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),  # ¡Esta línea es crucial!
    """
        Esta línea de código importa un conjunto predefinido de URLs de Django que manejan la autenticación de usuarios.
        En lugar de que tengas que escribir vistas y URLs para funciones comunes como login, logout, password_reset, password_reset_done, etc.
        Django te las proporciona ya hechas y listas para usar.
    """
    path('signup/', SignUpView.as_view(), name='signup'),
]
    