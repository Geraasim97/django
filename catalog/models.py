

from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='продукт')
    description = models.TextField(max_length=300, verbose_name='описание')



    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='продукт')
    description = models.TextField(max_length=300, verbose_name='описание')
    image = models.ImageField(upload_to='categories/', verbose_name='изображение (превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.price} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)

class Contacts(models.Model):
    contact_name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.contact_name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"



class Version(models.Model):
    """Версия продукта"""
    number = models.PositiveSmallIntegerField(verbose_name='Номер')
    title = models.CharField(max_length=100, verbose_name='Наименование')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    is_active = models.BooleanField(verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.number}: {self.title}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
