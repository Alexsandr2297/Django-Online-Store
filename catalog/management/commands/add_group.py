from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = 'Создает группу "Модератор продуктов" и назначает права.'

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='Модератор продуктов')

        # Получаем content type для модели Product
        content_type = ContentType.objects.get_for_model(Product)

        # Безопасно получаем разрешения
        unpublish_permission = Permission.objects.get(codename='can_unpublish_product',content_type=content_type)
        delete_permission = Permission.objects.get(codename='delete_product',content_type=content_type)

        if created:
            group.permissions.add(unpublish_permission, delete_permission)
            self.stdout.write(self.style.SUCCESS(
                'Группа "Модератор продуктов" создана и права добавлены.'))
        else:
            # Если группа уже существует, можно добавить права (на случай, если их нет)
            group.permissions.add(unpublish_permission, delete_permission)
            self.stdout.write(self.style.WARNING(
                'Группа уже существовала. Права добавлены/обновлены.'))
