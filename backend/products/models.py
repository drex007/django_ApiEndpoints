from django.db import models

# Create your models here
class Product(models.Model):
    title = models.CharField(max_length= 120,)
    content = models.TextField(blank= True, null = True)
    price = models.DecimalField(default=99.9, decimal_places=2, max_digits=15)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)* 0.8)

    def get_discount(self):
        return "122"