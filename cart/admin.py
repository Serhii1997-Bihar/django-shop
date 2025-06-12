from django.contrib import admin
from cart.models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ['order', 'product', 'quantity', 'size']
    extra = 0

class OrderModelAdmin(admin.ModelAdmin):
    readonly_fields = ['name', 'address', 'phone', 'mail', 'total_price', 'created_at', 'comment']
    inlines = [OrderItemInline]

admin.site.register(ClientData, OrderModelAdmin)
