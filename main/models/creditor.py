from django.db import models

class Creditor(models.Model):
    name = models.TextField(max_length='32')

    class Meta:
        verbose_name = 'Acreedor'
        verbose_name_plural = 'Acreedores'

    def __str__(self):
        return self.name