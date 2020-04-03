from django.contrib import admin

# Register your models here.
from .models import Product, ProductImage

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'#依照更新時間，等級排序
    search_fields = ['title','remark']#查詢欄位
    list_display = ['title','price','remark','active','updated']
    list_editable = ['price','active']
    list_filter = ['price','active']
    readonly_fields = ['timestamp','updated']
    prepopulated_fields = {"slug":("title",)}
    class Meta:
        model = Product

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)