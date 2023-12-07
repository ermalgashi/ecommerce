from django.db import models

# Create your models here.


class Product(models.Model):
    # Basic product information
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True)

    # Category can be a foreign key if you have a separate Category model
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # Additional fields like SKU, dimensions, weight, etc., can be added as needed
    sku = models.CharField(max_length=50, unique=True)
    weight = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=100, null=True, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # Additional methods can be added as needed, for example:
    # - Check if the product is in stock
    # - Update stock levels
    # - Apply discounts
