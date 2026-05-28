from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from .services import CatalogService
from django.core.cache import cache
from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .forms import ProductForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden


def products_by_category_view(request, category_id):
    """Отображает список продуктов в категории."""
    products = CatalogService.get_products_by_category(category_id)
    return render(request, 'products_by_category.html', {'products': products})


class PromoteProductView(LoginRequiredMixin, View):
    """Снимает продукт с публикации (требует прав can_unpublish_product)."""

    def post(self, request, pk):
        """Обрабатывает POST-запрос на снятие продукта с публикации."""
        product = get_object_or_404(Product, pk=pk)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("Пользователь не имеет нужного права на отмену")

        # Отменяем публикацию
        product.published_status = False
        product.save()

        return redirect('catalog:catalog_list')


class DeleteProductView(LoginRequiredMixin, View):
    """Удаляет продукт (требует права delete_product)."""

    def post(self, request, pk):
        """Обрабатывает POST-запрос на удаление продукта."""
        product = get_object_or_404(Product, id=pk)

        # Проверка права на удаление
        if not request.user.has_perm('catalog.delete_product'):
            return HttpResponseForbidden("У вас нет права на удаление продукта")

        product.delete()

        return redirect('catalog:catalog_list')


class ProductListView(ListView):
    """Список всех продуктов с низкоуровневым кешем на 15 мин."""

    model = Product
    template_name = 'catalog_list.html'
    context_object_name = 'catalogs'

    def get_queryset(self):
        """Возвращает кешированный список продуктов."""
        queryset = cache.get('products_all')
        if not queryset:
            print("Беру из БД")
            queryset = super().get_queryset()
            cache.set('products_all', queryset, 60 * 15)  # Кешируем данные на 15 минут
        else:
            print("Беру из КЭШ")
        return queryset


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Создаёт новый продукт."""

    model = Product
    form_class = ProductForm
    template_name = 'catalog_form.html'
    success_url = reverse_lazy('catalog:catalog_list')

    def form_valid(self, form):
        """Устанавливает текущего пользователя как владельца продукта."""
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирует продукт (только для владельца)."""

    model = Product
    form_class = ProductForm
    template_name = 'catalog_form.html'
    success_url = reverse_lazy('catalog:catalog_list')

    def dispatch(self, request, *args, **kwargs):
        """Проверяет, что пользователь является владельцем продукта."""
        product = self.get_object()

        if request.user != product.owner:
            return HttpResponseForbidden("У вас нет прав для редактирования этого продукта.")

        return super().dispatch(request, *args, **kwargs)


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(DetailView):
    """Детальная страница продукта с кешем страницы на 15 мин."""

    model = Product
    template_name = 'catalog_detail.html'
    context_object_name = 'catalog'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Удаляет продукт (владелец или модератор)."""

    model = Product
    template_name = 'catalog_confirm_delete.html'
    success_url = reverse_lazy('catalog:catalog_list')

    def dispatch(self, request, *args, **kwargs):
        """Проверяет права на удаление (владелец или модератор)."""
        product = self.get_object()

        if request.user != product.owner and not request.user.groups.filter(name='Модератор продуктов').exists():
            return HttpResponseForbidden("У вас нет прав для удаления этого продукта.")

        return super().dispatch(request, *args, **kwargs)
