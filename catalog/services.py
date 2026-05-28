from .models import Product
from django.core.cache import cache



class CatalogService:
    """Сервис для работы с продуктами."""
    
    @staticmethod
    def get_products_by_category(category_id):
        """Возвращает список продуктов в категории 15 мин."""
        cache_key = f'products:category:{category_id}'
        products = cache.get(cache_key)

        if not products:
            products = Product.objects.filter(category_id=category_id)
            cache.set(cache_key, products, 60 * 15)

        return products
