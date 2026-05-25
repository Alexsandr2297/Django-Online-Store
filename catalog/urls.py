from django.urls import path
from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='catalog_detail'),  # убрал лишний catalog/
    path('create/', ProductCreateView.as_view(), name='catalog_create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='catalog_update'),
    path('delete/<int:pk>/', views.DeleteProductView.as_view(), name='delete_product'),
    path('unpublish/<int:pk>/', views.PromoteProductView.as_view(), name='unpublish_product'),
    # Стандартный DeleteView с подтверждением
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='catalog_delete'),
    path('delete/<int:pk>/', views.DeleteProductView.as_view(), name='delete_product'),
]