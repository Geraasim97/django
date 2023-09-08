from django.core.management import BaseCommand
import os
from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        return os.system("python manage.py loaddata data.json")