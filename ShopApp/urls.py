from django.urls import path
from . import views

app_name = 'ShopApp'
urlpatterns = [
    path('catalog', views.catalog, name='catalog'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('add.<int:item_id>/', views.add_item, name='add'),
    path('cart', views.cart, name='cart'),
    path('clear', views.clear_cart, name='clear'),
    path('order', views.order, name='order'),
]