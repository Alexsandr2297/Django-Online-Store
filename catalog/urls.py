from django.urls import path
from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    products_by_category_view

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='catalog_detail'),
    path('create/', ProductCreateView.as_view(), name='catalog_create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='catalog_update'),
    path('delete/<int:pk>/', views.DeleteProductView.as_view(), name='delete_product'),
    path('unpublish/<int:pk>/', views.PromoteProductView.as_view(), name='unpublish_product'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='catalog_delete'),
    path('delete/<int:pk>/', views.DeleteProductView.as_view(), name='delete_product'),
    path('category/<int:category_id>/', products_by_category_view, name='products_by_category')
]