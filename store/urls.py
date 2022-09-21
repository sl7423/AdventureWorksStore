from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProductList.as_view(), name='store'),
    path('category/<productcategoryid>', views.ProductListByCategoryView.as_view(), name='product_by_category'),
    path('category/<productcategoryid>/subcategory/<productsubcategoryid>', views.ProductNewView.as_view(), name='product'),
    path('category/<productcategoryid>/subcategory/<productsubcategoryid>/product/<productid>', views.ProductDetailView.as_view(), name='product_details'),
    path('search/', views.Search.as_view(), name='search'),
]