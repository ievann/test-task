from django.db import models

# Create your models here.

class Data(models.Model):
    code = models.CharField(max_length=32)              # Код
    name = models.CharField(max_length=64)              # Наименование
    #level1 = models.CharField()                        # Уровни вложенности
    #level2 = models.CharField()
    #level3 = models.CharField()
    price = models.PositiveIntegerField()               # Цена
    priceSP = models.PositiveIntegerField()             # ЦенаСП
    quantity = models.PositiveIntegerField()            # Количество
    value_fields = models.CharField(max_length=64)      # Поля свойств
    #joint_purchases = models.ForeignKey(self)          # Совместные покупки
    measurment_unit = models.CharField(max_length=16)   # Единица измерения
    picture = models.CharField(max_length=64)           # Картинка
    show_on_mainpage = models.BooleanField()            # Выводить на главной
    description = models.TextField()                    # Описание
