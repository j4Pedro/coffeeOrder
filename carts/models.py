from django.db import models

# Create your models here.
from products.models import Product

class CartItem(models.Model):
    cart = models.ForeignKey('Cart',on_delete=models.CASCADE,null=True,blank=True,)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="數量",default=1) 
    line_total = models.DecimalField(max_digits=100,decimal_places=2, default=9.99)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name="成立日期")
    updated = models.DateTimeField(auto_now_add=False,auto_now=True,verbose_name="更新日期")
   
    def __unicode__(self):
        try:
            return self.cart.id
        except:
            return self.product.title

class Cart(models.Model):
    #items = models.ManyToManyField(CartItem,blank=True)
    #products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(max_digits=100,decimal_places=2, default=0.00 ,verbose_name="總金額")
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name="成立日期")
    updated = models.DateTimeField(auto_now_add=False,auto_now=True,verbose_name="更新日期")
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.id
