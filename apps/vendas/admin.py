from django.contrib import admin
from .models import Venda
from .models import Venda, ItemVenda

class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1

class VendaAdmin(admin.ModelAdmin):
    inlines = [ItemVendaInline]

admin.site.register(Venda, VendaAdmin)
admin.site.register(ItemVenda)