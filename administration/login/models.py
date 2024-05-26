from django.db import models

MAX_LENGTH_NAME: int = 50
MAX_LENGTH_EMAIL: int = 100


ROLE_OPTIONS: dict = {
    'adm': 'Administrador',
    'don': 'Doador',
    'aux': 'Auxiliado'
}


class User(models.Model):
    name: str = models.CharField(max_length=MAX_LENGTH_NAME)
    email: str = models.EmailField(max_length=MAX_LENGTH_EMAIL)
    role: str = models.TextField(choices=ROLE_OPTIONS)
