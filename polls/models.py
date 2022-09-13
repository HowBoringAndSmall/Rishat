from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=400, blank=True)
    price = models.IntegerField()
    orders = models.ManyToManyField('Order', related_name='items')
    currency = models.CharField(max_length=10, default='usd')

    def __str__(self):
        return self.name


class Order(models.Model):
    ip = models.GenericIPAddressField()
