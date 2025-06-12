from django.db import models
from shop.models import *

class OrderItem(models.Model):
    order = models.ForeignKey('ClientData', on_delete=models.CASCADE, verbose_name='Дані клієнта')
    product = models.ForeignKey(ProductsModel, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(verbose_name='Кількість')
    size = models.CharField(max_length=50, verbose_name='Розмір', blank=True)

    class Meta:
        verbose_name_plural = 'Товари'
        verbose_name = 'Товар'

    def __str__(self):
        return self.product.name

class ClientData(models.Model):
    order_number = models.PositiveIntegerField(default=1, unique=True, editable=False)
    name = models.CharField(max_length=255, verbose_name='Назва продукту')
    address = models.CharField(max_length=255, verbose_name='Адреса')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    mail = models.EmailField(blank=True, verbose_name='Електронна пошта')
    comment = models.TextField(blank=True, verbose_name='Коментар')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Сума замовлення')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата формування')

    class Meta:
        verbose_name_plural = 'Замовлення'
        verbose_name = 'Замовлення'

    def __str__(self):
        return f'Замовлення N{self.order_number} від {self.created_at.strftime("%d.%m.%Y %H:%M")}'
