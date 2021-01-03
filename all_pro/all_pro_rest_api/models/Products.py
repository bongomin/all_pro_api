from django.db import models

# Create your models here.
class ProductsModel(models.Model):
    CATEGORY = (
        ('DRINKS','DRINKS'),
        ('FOOD', 'FOOD'),
        ('BEVERAGES', 'BEVERAGES'),
        ('BREAD','BREAD'),
        ('DAIRY', 'DAIRY'),
        ('OTHERS', 'OTHERS')
    )
    product_name = models.CharField(max_length=100)
    unit_price = models.CharField(max_length=100)
    product_type = models.CharField(max_length=90)
    quantity = models.CharField(max_length=100)
    product_category = models.CharField(choices=CATEGORY, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


