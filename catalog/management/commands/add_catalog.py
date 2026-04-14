from django.core.management.base import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):


    help = 'Loads test products into the database'


def handle(self, *args, **kwargs):
    Product.objects.all().delete()
    Category.objects.all().delete()

    cat_smartphones = Category.objects.create(name='РЎРјР°СЂС‚С„РѕРЅС‹',
                                              description='Р»СѓС‡С€РёРµ СЃРјР°СЂС‚С„РѕРЅС‹ РІ РјРёСЂРµ')
    cat_tvs = Category.objects.create(name='РўРµР»РµРІРёР·РѕСЂС‹',
                                      description='Р»СѓС‡С€РёРµ С‚РµР»РµРІРёР·РѕСЂС‹ РІ РјРёСЂРµ')

    # РЎРѕР·РґР°РµРј РїСЂРѕРґСѓРєС‚С‹, РёСЃРїРѕР»СЊР·СѓСЏ СЃРѕР·РґР°РЅРЅС‹Рµ РєР°С‚РµРіРѕСЂРёРё
    Product.objects.create(
        name='Honor',
        description='РјРѕС‰РЅС‹Р№ СЃРјР°СЂС‚С„РѕРЅ',
        price=40000,
        category=cat_smartphones
    )
    Product.objects.create(
        name='Xiaomi',
        description='РєР°С‡РµСЃС‚РІРµРЅРЅС‹Р№ С‚РµР»РµРІРёР·РѕСЂ',
        price=35000,
        category=cat_tvs
    )

    self.stdout.write(self.style.SUCCESS('Successfully added test products'))
