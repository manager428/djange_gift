from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'profile_pic']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'category', 'brand', 'price', 'stock', 'tag', 'product_img']

class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'qty', 'price', 'amount']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['code', 'user', 'first_name', 'last_name','house_no', 'street', 'city', 'pin', 'state', 'total', 'placed_at']

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['order','user' , 'product', 'price', 'qty', 'amount', 'status']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
admin.site.register(Review)
admin.site.register(Wishlist)