from django.db import models

# Create your models here.

class Data(models.Model):
    code = models.CharField(max_length=32)              # Код
    name = models.CharField(max_length=64)              # Наименование
    level1 = models.CharField(max_length=64,\
            blank = True)                               # Уровни вложенности
    level2 = models.CharField(max_length=64,\
            blank = True)
    level3 = models.CharField(max_length=64,\
            blank = True)
    # DecimalField doesn't accept comma separated decimals
    # FloatField isn't for money and doesn't accept commas
    price = models.DecimalField(max_digits=10,\
            decimal_places=2)                           # Цена
    priceSP = models.DecimalField(max_digits=10,\
            decimal_places=2)                           # ЦенаСП
    # Uncomment if it is necessary to preserve
    # both prices as comma separated strings
#    price = models.CharField(max_length=16)             # Цена
#    priceSP = models.CharField(max_length=16)           # ЦенаСП
    quantity = models.PositiveIntegerField()            # Количество
    value_fields = models.CharField(max_length=64)      # Поля свойств
    #joint_purchases = models.ForeignKey(self)          # Совместные покупки
    measurment_unit = models.CharField(max_length=16)   # Единица измерения
    picture = models.CharField(max_length=64)           # Картинка
    show_on_mainpage = models.BooleanField()            # Выводить на главной
    description = models.TextField()                    # Описание
