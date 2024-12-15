from django.contrib import admin
from MabatiApp.models import Product, ImageModel, Category, Contact, CartItem, Register

# Register your models here.
admin.site.register(Product)
admin.site.register(ImageModel)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(CartItem)
admin.site.register(Register)