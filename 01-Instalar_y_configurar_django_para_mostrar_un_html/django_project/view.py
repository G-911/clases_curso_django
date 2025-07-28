# Importamos TemplateView desde django.views.generic.
# TemplateView es una clase preconstruida en Django que nos permite renderizar una plantilla HTML sin necesidad de lógica adicional en la vista.
from django.views.generic import TemplateView

# Definimos una clase llamada HomeView que hereda de TemplateView.
# Esta será nuestra vista basada en clases (CBV = Class-Based View), y su propósito principal es mostrar la página "home.html" al usuario.
class HomeView(TemplateView):
    
    # Atributo obligatorio para TemplateView: le indicamos cuál plantilla HTML debe renderizar.
    # En este caso, la plantilla se llama "home.html" y debe estar ubicada en la carpeta de templates del proyecto.
    template_name = "home.html"