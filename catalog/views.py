from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProductForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ProductListView(ListView):
    model = Product
    template_name = 'catalog_list.html'
    context_object_name = 'catalogs'


class ProductCreateView(LoginRequiredMixin ,CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog_form.html'
    success_url = reverse_lazy('catalog:catalog_list')


class ProductUpdateView(LoginRequiredMixin ,UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog_form.html'
    success_url = reverse_lazy('catalog:catalog_list')



class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog_detail.html'
    context_object_name = 'catalog'


class ProductDeleteView(LoginRequiredMixin ,DeleteView):
    model = Product
    template_name = 'catalog_confirm_delete.html'
    success_url = reverse_lazy('catalog:catalog_list')
