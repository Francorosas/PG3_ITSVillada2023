from django.urls import path
from .views import consultar_clima

urlpatterns = [
    path('', consultar_clima, name='consultar_clima'),
]