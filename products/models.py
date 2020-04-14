from django.db import models


# Create your models here.
class Product(models.Model):
    # id 有預設 uid
    title = models.CharField(max_length=100,verbose_name="品名")
    price = models.DecimalField(max_digits=100,decimal_places=2,verbose_name="價格")
    slug = models.SlugField(unique=True) #不支援中文
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name="成立日期")
    updated = models.DateTimeField(auto_now_add=False,auto_now=True,verbose_name="更新日期")
    active = models.BooleanField(default=True)
    remark = models.TextField(null=True,blank=True,verbose_name="說明")

    def __str__(self):
        return self.title
    
    class Meta:
        unique_together = ('title','slug')

    def get_price(self):
        return self.price
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("single_product",kwargs={"slug":self.slug})

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/', verbose_name="產品圖片")
    featured = models.BooleanField(default=False,verbose_name='精選')
    thumbnail = models.BooleanField(default=False,verbose_name='縮圖')
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True,verbose_name="更新日期")

    def __str__(self):
        return self.product.title

class VariationManager(models.Model):
    def all(self):
        return super(VariationManager, self).filter(active=True)
    def sizes(self):
        return self.all().filter(category='size')
    def areas(self):
        return self.all().filter(category='area')


VAR_CATEGORIES =(
    ('size','size'),
    ('area','area'),
    ('package','package'),
    )

class Variation(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    category = models.CharField(max_length=120,choices=VAR_CATEGORIES,default='size')
    title = models.CharField(max_length=120)
    image = models.ForeignKey(ProductImage, null=True,blank=True,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=100,decimal_places=2,null=True,blank=True,verbose_name="價格")
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True,verbose_name="更新日期")

    objects = VariationManager()

    def __str__(self):
        return self.title

