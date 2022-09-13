from django.contrib import admin
from .models import Item, Order

admin.site.register(Item)


class ItemInLine(admin.TabularInline):
    model = Item.orders.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('ip', )
    inlines = (ItemInLine, )