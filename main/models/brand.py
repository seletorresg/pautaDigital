from django.db import models
from django.db.models.deletion import SET_NULL

from main.models.client import Client

class Brand(models.Model):
    name = models.TextField(max_length='32')
    client_id = models.ForeignKey(Client, on_delete=SET_NULL, null=True)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.name