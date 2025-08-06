from django.contrib import admin
from .models import Customer, Connection, Bill, Payment

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact', 'city', 'state')
    search_fields = ('first_name', 'last_name', 'email', 'contact')

@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ('connection_id', 'customer', 'connection_type', 'start_date', 'is_active')
    list_filter = ('connection_type', 'is_active')
    search_fields = ('connection_id', 'customer__first_name', 'customer__last_name')

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'connection', 'month', 'year', 'total_units', 'is_paid')
    list_filter = ('is_paid', 'month', 'year')
    search_fields = ('connection__connection_id', 'connection__customer__first_name')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'bill', 'amount', 'payment_date')
    list_filter = ('payment_date',)
    search_fields = ('bill__id', 'card_number')