from django.contrib import (
    admin,
)  # Importa el módulo 'admin' de Django. Este es el corazón del panel de administración.
from .models import (
    Post,
)  # Importa tu modelo 'Post' desde el archivo models.py de la misma aplicación.

# Aquí es donde le dices a Django qué modelos de tu aplicación quieres que aparezcan
# en el panel de administración. Esto es muy útil para gestionar tus datos
# (crear, leer, actualizar, borrar posts) sin escribir código SQL.

# Registramos el modelo 'Post'.
# Al hacer esto, Django automáticamente creará una interfaz de administración
# para tu modelo 'Post' en el panel de administración.
# ¡Ahora podrás ver y gestionar tus posts fácilmente desde el navegador!
admin.site.register(Post)
