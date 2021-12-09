from django.urls import path

from core.api.serializers import ItemSerializer
from .views import ItemListView

urlpatterns = [
    path('product-list/', ItemListView.as_view(), name='product-list')

]
