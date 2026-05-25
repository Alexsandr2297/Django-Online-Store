from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .forms import ProductForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden


class PromoteProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("Пользователь не имеет нужного права на отмену")


        # Отменяем публикацию
        product.published_status = False
        product.save()

        return redirect('catalog:catalog_list')


class DeleteProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        # Проверка права на удаление
        if not request.user.has_perm('catalog.delete_product'):
            return HttpResponseForbidden("У вас нет права на удаление продукта")

        product.delete()

        return redirect('catalog:catalog_list')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog_list.html'
    context_object_name = 'catalogs'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog_form.html'
    success_url = reverse_lazy('catalog:catalog_list')


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog_form.html'
    success_url = reverse_lazy('catalog:catalog_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()

        if request.user != product.owner:
            return HttpResponseForbidden("У вас нет прав для редактирования этого продукта.")

        return super().dispatch(request, *args, **kwargs)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog_detail.html'
    context_object_name = 'catalog'


class ProductDeleteView(LoginRequiredMixin ,DeleteView):
    model = Product
    template_name = 'catalog_confirm_delete.html'
    success_url = reverse_lazy('catalog:catalog_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()

        if request.user != product.owner and not request.user.groups.filter(name='Модератор продуктов').exists():
            return HttpResponseForbidden("У вас нет прав для удаления этого продукта.")

        return super().dispatch(request, *args, **kwargs)
