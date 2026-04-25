from django.contrib import admin
from .models import Bag, BagItem


@admin.register(Bag)
class BagAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at', 'get_total_items')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__username',)
    readonly_fields = ('created_at', 'updated_at')

    def get_total_items(self, obj):
        return obj.get_total_items()
    get_total_items.short_description = 'Total Items'


@admin.register(BagItem)
class BagItemAdmin(admin.ModelAdmin):
    list_display = ('card', 'bag', 'quantity', 'get_subtotal')
    list_filter = ('added_at', 'bag__user')
    search_fields = ('card__name', 'bag__user__username')
    readonly_fields = ('added_at',)

    def get_subtotal(self, obj):
        return f"${obj.get_subtotal()}"
    get_subtotal.short_description = 'Subtotal'
