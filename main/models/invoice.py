from datetime import timezone
from django.db import models
from django.db.models.deletion import SET_NULL
from django.utils.timezone import now as timezone_now
import os

from main.models.currency import Currency
from main.models.plan import Plan
from main.models.investment import Investment

def upload_invoice(instance,filename):
    now = timezone_now()
    filename_base, filename_ext = os.path.splitext(filename)
    time_stamp = now.strftime("%d%H%M%S")
    pk = instance.invoice_number
    return "files/facturas/%s_%s%s" % (pk,time_stamp,filename_ext.lower())

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=16)
    value = models.FloatField()
    currency = models.ForeignKey(Currency, on_delete=SET_NULL, null=True, blank=True)
    date = models.DateField()
    plan = models.ForeignKey(Plan, on_delete=SET_NULL, null=True, blank=True)
    investment = models.ForeignKey(Investment,on_delete=SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to=upload_invoice)

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return self.invoice_number