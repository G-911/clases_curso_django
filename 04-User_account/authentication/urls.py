from django.contrib import admin
from django.urls import path, include
from .views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),  # ¡Esta línea es crucial!
    path('signup/', SignUpView.as_view(), name='signup'),
]
    