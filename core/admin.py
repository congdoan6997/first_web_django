from django.contrib import admin
from .models import Item, Oder, OderItem


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount_price', 'category', 'label']
    list_filter = ['category']
    search_fields = ['title']


# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Oder)
admin.site.register(OderItem)
