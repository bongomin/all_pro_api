from django.db import models

# Create your models here.
class ProductsModel(models.Model):
    CATEGORY = (
        ('C','CARBOHYDRATES'),
        ('F','FRUITS'),
        ('D','DRINKS'),
        ('FO','FOOD'),
        ('N','NO_CATEGORY')
    )
    product_name = models.CharField(max_length=100)
    unit_price = models.CharField(max_length=100)
    product_type = models.CharField(max_length=90)
    quantity = models.CharField(max_length=100)
    product_category = models.CharField(choices=CATEGORY, max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


