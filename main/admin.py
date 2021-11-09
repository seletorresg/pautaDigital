from django.contrib import admin
from main.models import *

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Commission)
class CommissionAdmin(admin.ModelAdmin):
    pass

@admin.register(Creditor)
class CreditorAdmin(admin.ModelAdmin):
    pass

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass

@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    pass