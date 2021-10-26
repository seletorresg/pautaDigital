from django.db import models

class Commission(models.Model):
    name = models.TextField(max_length='32')
    percentage = models.FloatField()

    class Meta:
        verbose_name = 'Comision'
        verbose_name_plural = 'Comisiones'

    def __str__(self):
        return self.name