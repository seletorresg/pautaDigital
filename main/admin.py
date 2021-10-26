from django.contrib import admin
from main.models import *

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Client,ClientAdmin)

class BrandAdmin(admin.ModelAdmin):
    pass

admin.site.register(Brand,BrandAdmin)

class InvoiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Invoice,InvoiceAdmin)

class CommissionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Commission,CommissionAdmin)

class CreditorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Creditor,CreditorAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Currency,CurrencyAdmin)

class InvestmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Investment,InvestmentAdmin)

class PlanAdmin(admin.ModelAdmin):
    pass

admin.site.register(Plan,PlanAdmin)