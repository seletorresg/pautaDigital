from django.db import models
from django.db.models.deletion import SET_NULL
from django.utils.timezone import now as timezone_now
import os

from main.models.currency import Currency
from main.models.plan import Plan
from main.models.investment import Investment

def upload_invoice(instance,filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return "plan%s_%s_%s" % (instance.plan_id,instance.investment_id,instance.invoice_number,filename,filename_ext.lower())

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=16)
    value = models.FloatField()
    currency_id = models.ForeignKey(Currency, on_delete=SET_NULL, null=True, blank=True)
    date = models.DateField()
    plan_id = models.ForeignKey(Plan, on_delete=SET_NULL, null=True, blank=True)
    investment_id = models.ForeignKey(Investment,on_delete=SET_NULL, null=True, blank=True)
    document = models.FileField(upload_to=upload_invoice)

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return self.invoice_number