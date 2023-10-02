from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from store.views import user_login, user_logout, product_list, add_to_cart, remove_from_cart, update_cart, place_order, product_detail, add_product, edit_product, delete_product, search_products, filter_products, category_list, tag_list, cart, orders


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('', product_list, name='product_list'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('cart/', remove_from_cart, name='view_cart'),
    path('update_cart/<int:cart_id>/', update_cart, name='update_cart'),
    path('place_order/', place_order, name='place_order'),
    path('product/', product_detail, name='product_detail'),
    path('product/add/', add_product, name='add_product'),
    path('product/edit/', edit_product, name='edit_product'),
    path('product/delete/', delete_product, name='delete_product'),
    path('search/', search_products, name='search_products'),
    path('filter/', filter_products, name='filter_products'),
    path('category/', category_list, name='category_list'),
    path('tag/', tag_list, name='tag_list'),
    path('cart/', cart, name='cart'),
    path('orders/', orders, name='orders'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)