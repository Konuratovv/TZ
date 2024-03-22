from django.db import models

# Create your models here.

STATUS_CHOICES = [
    ('BR', 'Бронь'),
    ('AC', 'Активно'),
    ('PU', 'Куплено'),
    ('BA', 'Бартер'),
    ('IN', 'Рассрочка'),
    ('CA', 'Отменено'),
]

class Object(models.Model):
    title = models.CharField(max_length = 150, verbose_name='Объект')

class Appartments(models.Model):
    object = models.ForeignKey("appartments.Object", verbose_name='Объект', on_delete=models.CASCADE)
    floor = models.PositiveIntegerField(verbose_name='Этаж')
    kv = models.DecimalField(max_digits=7, decimal_places=1 ,verbose_name='КВ')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, verbose_name='Статус')
    price = models.IntegerField(verbose_name='Цена')
    customer = models.CharField(max_length=150, verbose_name='Клиент')
    customer_number = models.CharField(max_length=150, verbose_name='Номер клиента')
    contract_number = models.IntegerField(verbose_name='Номер договора')
    end_time = models.DateTimeField(verbose_name='Время окончания')

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"