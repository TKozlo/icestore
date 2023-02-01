from django.contrib import admin

from products.models import Product, ProductCategory, Basket 
# Register your models here.

admin.site.register(ProductCategory)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ('name', 'price', 'quantity', 'category')
   fields = ('image', 'name', 'description', ('price', 'quantity'), 'stripe_product_price_id','category')
   #readonly_fields = ('description',)
   search_fields = ('name',)
   ordering = ('-name',)



class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
    readonly_fields = ('created_timestamp',)
    extra = 0

