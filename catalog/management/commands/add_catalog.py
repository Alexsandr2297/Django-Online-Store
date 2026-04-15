from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Loads test products into the database'

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()
        Category.objects.all().delete()


        cat_smartphones = Category.objects.create(name='Смартфоны', description='лучшие смартфоны в мире')
        cat_tvs = Category.objects.create(name='Телевизоры', description='лучшие телевизоры в мире')

        # Создаем продукты, используя созданные категории
        Product.objects.create(
            name='Honor',
            description='мощный смартфон',
            price=40000,
            category=cat_smartphones
        )
        Product.objects.create(
            name='Xiaomi',
            description='качественный телевизор',
            price=35000,
            category=cat_tvs
        )

        self.stdout.write(self.style.SUCCESS('Successfully added test products'))
