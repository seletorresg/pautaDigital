from django.db import models

class Client(models.Model):
    name = models.TextField(max_length='32')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name