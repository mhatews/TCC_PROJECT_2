from django.contrib import admin


from .models import Ordem, ItemOrdem

class ItemOrdemInline(admin.TabularInline):
    model = ItemOrdem
    extra = 1

class OrdemAdmin(admin.ModelAdmin):
    inlines = [ItemOrdemInline]

admin.site.register(Ordem, OrdemAdmin)
admin.site.register(ItemOrdem)
