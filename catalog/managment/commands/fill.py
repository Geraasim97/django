from django.core.management import BaseCommand, call_command
import os
from catalog.models import Category, Product

import os

from django.core.management import BaseCommand




class Command(BaseCommand):

    def handle(self, *args, **options):
        products_list = [
            {'product_name': 'Яблоки', 'description': 'Российские яблоки', 'category_id': 6, 'price': 100},
            {'product_name': 'Макароны', 'description': 'Макароны из муки высшего сорта', 'category_id': 7,
             'price': 124},
            {'product_name': 'Килька', 'description': 'Килька в томатном соусе', 'category_id': 8, 'price': 35},
            {'product_name': 'Сахар', 'description': 'Сахар тростниковый', 'category_id': 7, 'price': 70},
            {'product_name': 'Соль', 'description': 'Соль морская, поваренная', 'category_id': 7, 'price': 80},


        ]
        Product.objects.all().delete()
        for product in products_list:

            Product.objects.create(**product)











class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        call_command('loaddata', 'catalog_data.json')