from django.urls import path
from catalog.views import home
from catalog.views import contacts

app_name = 'templates'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
]
