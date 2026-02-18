from django.urls import path
from . import views

urlpatterns = [
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('company/<slug:slug>/', views.company_detail, name='company_detail'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('buy-now/<int:product_id>/', views.buy_now, name='buy_now'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

]
