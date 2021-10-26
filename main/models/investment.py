from django.db import models
from django.db.models.deletion import SET_NULL
from main.models.brand import Brand
from main.models.client import Client
from main.models.commission import Commission

class Investment(models.Model):
    months_choices = [
        ('Enero','Enero'),
        ('Febrero','Febrero'),
        ('Marzo','Marzo'),
        ('Abril','Abril'),
        ('Mayo','Mayo'),
        ('Junio','Junio'),
        ('Julio','Julio'),
        ('Agosto','Agosto'),
        ('Septiembre','Septiembre'),
        ('Octubre','Octubre'),
        ('Noviembre','Noviembre'),
        ('Diciembre','Diciembre'),
    ]
    campaign = models.TextField(max_length='32')
    medio = models.TextField(max_length='32')
    format = models.TextField(max_length='32')
    client_id = models.ForeignKey(Client, on_delete=SET_NULL, null=True)
    brand_id = models.ForeignKey(Brand, on_delete=SET_NULL, null=True)
    value = models.FloatField()
    comission = models.ForeignKey(Commission, on_delete=SET_NULL, null=True)
    available_value = models.FloatField()
    month = models.TextField(choices=months_choices)
    year = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Inversion'
        verbose_name_plural = 'Inversiones'

    def __str__(self):
        name =  self.campaign + '-' + self.medio + '-' + self.format + '-' + self.month + '-' + str(self.year)
        return name