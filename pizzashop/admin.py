from django.contrib import admin
from pizzashop.models import Customer, Order, Item, OrderItem, BasketItem


class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.fields]
    search_fields = ['phone', 'address', 'last_name']
    list_filter = ['phone']

    class Meta:
        model = Customer


class ItemAdmin (admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'image_tag']
    fields = ('title', 'description', 'price', 'image', 'image_tag')
    readonly_fields = ('image_tag',)
    search_fields = ['title', 'price', 'description']
    list_filter = ['price']

    class Meta:
        model = Item

    class Media:
        js = ('admin/js/admin.js',)
        css = {
            'all': ('admin/css/admin.css',)
        }


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    search_fields = ['customer__id', 'customer__phone', 'customer__address', 'customer__last_name', 'status']
    list_filter = ['status', 'customer__id', 'customer__phone']


class OrderItemAdmin (admin.ModelAdmin):
    list_display = [field.name for field in OrderItem._meta.fields]
    search_fields = ['item__id', 'order__id', 'count', 'price_per_item', 'total_price', 'is_active', 'created', 'updated']
    list_filter = ['order__id', 'order__customer__phone']

    class Media:
        js = ('admin/js/admin.js',)
        css = {
            'all': ('admin/css/admin.css',)
        }


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(BasketItem)
