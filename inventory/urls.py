from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import ItemViewSet, CategoryViewSet


router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'categories', CategoryViewSet)
urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('add/', views.item_add, name='item_add'),
    path('edit/<int:pk>/', views.item_edit, name='item_edit'),
    path('delete/<int:pk>/', views.item_delete, name='item_delete'),
    path('bulk_action/', views.bulk_action, name='bulk_action'),
    path('purchase/<int:pk>/', views.purchase_item, name='purchase_item'),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/remove/<int:cart_item_id>/', views.cart_remove, name='cart_remove'),
    path('checkout/', views.checkout, name='checkout'),
    path('', include(router.urls)),  # <-- Enables /items/ and /categories/


]
