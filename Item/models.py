from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=50,
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    price = models.FloatField(
        verbose_name='Цена',
        validators=[
            MinValueValidator(0),
        ]
    )
