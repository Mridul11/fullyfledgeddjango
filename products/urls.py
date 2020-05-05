from django.urls import path 
from django.contrib.auth.decorators import login_required
from products.views import ( 
    ProductListView, product_list_view, ProductDetailView, 
    product_detail_view, FeaturedProductListView )


urlpatterns = [
    path('featured-products/', FeaturedProductListView.as_view(), name="featured-products"),
    path('products/', ProductListView.as_view(), name="products"),
    path('products-fbv/', product_list_view, name="products-fbv"),
    path('products/<int:pk>', ProductDetailView.as_view(), name="products-detail"),
    path('products-fbv/<int:pk>', product_detail_view, name="products-detail-fbv"),
]
