from django.contrib import admin
from django.urls import path, include
from .views import SignUpView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),  # ¡Esta línea es crucial!
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='mi_app/login_personalizado.html'), name='login'), en casso de que quieran un login personalizado
]