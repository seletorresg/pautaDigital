from django.db import models
from django.db.models.deletion import SET_NULL
from main.models.creditor import Creditor
from main.models.client import Client
from main.models.brand import Brand

class Plan(models.Model):
    name = 'none'
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
    payment = [
        ('1','Interno'),
        ('2','Externo')
    ]
    client = models.ForeignKey(Client, on_delete=SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=SET_NULL, null=True)
    month = models.TextField(choices=months_choices)
    year = models.PositiveSmallIntegerField()
    type_of_pay = models.TextField(choices=payment)
    creditor = models.ForeignKey(Creditor, on_delete=SET_NULL, null=True)
    subtotal_available = models.FloatField()
    total_available = models.FloatField()
    total_invested = models.FloatField()
    total_comsissions = models.FloatField()

    class Meta:
        verbose_name = 'Plan de Medios'
        verbose_name_plural = 'Planes de Medios'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = self.client.name +'-'+self.brand.name +'-'+str(self.month) + '-' + str(self.year)

    def __str__(self):
        self.name = self.client.name +'-'+self.brand.name +'-'+str(self.month) + '-' + str(self.year)
        return self.name