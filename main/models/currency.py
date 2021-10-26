from django.db import models

class Currency(models.Model):
    name = models.TextField(max_length='32')
    symbol = models.TextField(max_length='4')

    class Meta:
        verbose_name = 'Moneda'
        verbose_name_plural = 'Monedas'

    def __str__(self):
        return self.name