from django.contrib import admin
from .models import Category, Card


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'get_image_preview')
    list_filter = ('category', 'price')
    search_fields = ('name', 'description')
    list_editable = ('price', 'quantity')
    
    fieldsets = (
        ('Card Info', {
            'fields': ('name', 'description', 'category')
        }),
        ('Inventory & Pricing', {
            'fields': ('quantity', 'price')
        }),
        ('Card Image', {
            'fields': ('image',),
            'description': 'Upload a clear image of the card. Recommended: 300x400px or similar aspect ratio'
        }),
    )
    
    readonly_fields = ('get_image_preview',)
    
    def get_image_preview(self, obj):
        """Display image preview in list view"""
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="70" style="object-fit: cover;" />'
        return 'No image'
    
    get_image_preview.short_description = 'Image'
    get_image_preview.allow_tags = True
