from django.db import (
    models,
)  # Importamos 'models' de Django, que nos permite definir modelos para nuestra base de datos.

# Aquí es donde definimos nuestros modelos. Un modelo es como un plano o esquema
# de cómo se verán los datos que queremos guardar en nuestra base de datos.


# Creamos una clase llamada 'Post'. Cada 'Post' que creemos en nuestra aplicación
# será un objeto basado en este plano.
# Heredamos de 'models.Model' para que Django sepa que esta clase es un modelo
# y pueda manejarla automáticamente (crear tablas en la base de datos, etc.).
class Post(models.Model):
    # Definimos los campos (columnas) de nuestro modelo 'Post'.

    # 'title' (título): Será un campo de texto para el título del post.
    # 'models.TextField()' es para texto largo, pero aquí el usuario puso 'max_length',
    # lo que sugiere que quiere un campo de texto más corto como 'CharField'.
    # Si el título es corto, 'CharField' es mejor. Si es largo, 'TextField'.
    # Para este ejemplo, mantendremos 'TextField' pero con 'max_length' como lo tenías.
    title = models.TextField(
        max_length=200
    )  # 'max_length' es el número máximo de caracteres que puede tener el título.

    # 'description' (descripción): Otro campo de texto, ideal para el contenido principal del post.
    # 'models.TextField()' se usa para textos largos, como el cuerpo de un artículo.
    description = models.TextField()

    # El método '__str__' es especial en Python.
    # Cuando Django necesite mostrar un objeto 'Post' (por ejemplo, en el panel de administración),
    # usará lo que este método retorne.
    # Aquí, le decimos que muestre el 'title' (título) del post, lo cual es muy útil
    # para identificar cada post fácilmente.
    def __str__(self):
        return self.title  # Retorna el título del post como su representación en texto.
