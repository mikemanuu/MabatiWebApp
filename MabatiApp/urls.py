from django.contrib import admin
from django.urls import path
from MabatiApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('about', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-confimation/', views.order_confirmation, name='order_confirmation'),
    path('contact/', views.contact, name='contact'),
    path('contact_view/', views.contact_view, name='contact_view'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('products/', views.products, name='products'),
    path('products/<str:category>/', views.products, name='products_by_category'),
    path('product_details/<int:product_id>/', views.product_details, name='product_details'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.image_delete),
    path('delete/<int:id>', views.delete),
    path('delete/<int:id>', views.delete),
    path('add_product/', views.add_product, name='add_product'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/<int:cart_item_id>/', views.update_cart, name='update_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('register/', views.register_user, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout_user/', views.logout_user, name='logout_user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)