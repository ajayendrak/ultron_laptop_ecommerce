from django.db import models
from django.db.models.fields import DateField
from django.db.models.fields.files import ImageField

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    price = models.IntegerField(default=1)
    desc = models.TextField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")
    
    class Meta:  
        db_table = "products" 

    def __str__(self):
        return self.product_name