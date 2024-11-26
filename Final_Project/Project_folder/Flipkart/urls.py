from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('search/', views.search, name='search'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('payment/', views.payment, name='payment'),
    path('single-payment/<int:product_id>/', views.single_payment, name='single_payment'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('address/', views.address_fillup, name='address'),
    path('single-address/', views.single_address, name='single_address'),
    path('placed-order/', views.placed_order , name = "placed_order"),
    
]
