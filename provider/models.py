from django.db import models
from django.contrib.auth.models import AbstractUser


class Supplier(models.Model):
    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    title = models.CharField(verbose_name='Название', max_length=50)
    email = models.EmailField()
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=200)
    building = models.IntegerField()
    product_name = models.CharField(max_length=200)
    product_model = models.TextField(verbose_name='Модель')
    date_created = models.DateTimeField()
    debts = models.DecimalField(verbose_name='Задолженность', max_digits=10, decimal_places=2, null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    suppliers = models.ForeignKey('self', verbose_name='Поставщик', null=True, blank=True, on_delete=models.CASCADE)


class Factory(Supplier):
    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'


class Retail(Supplier):
    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'


class Entrepreneur(Supplier):
    class Meta:
        verbose_name = 'Предприниматель'
        verbose_name_plural = 'Предприниматели'


class Employee(AbstractUser):
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

