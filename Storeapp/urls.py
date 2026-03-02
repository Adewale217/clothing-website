from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list, name='product_list'),
    path('test/', views.storeapp_view, name='storeapp'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup')
]
