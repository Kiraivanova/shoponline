from django.forms import ModelChoiceField
from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    change_form_template = 'change_form.html'
    #exclude = ('features',)


admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product, ProductAdmin)
