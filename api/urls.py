from django.urls import path
from . import views

urlpatterns = [
  path('header-image-list/', views.HeaderImageList.as_view(), name='header-image-list'),
  path('<int:pk>/', views.HeaderImageDetail.as_view(), name='header-image-detail'),
  path('create/', views.HeaderImageCreate.as_view(), name='header-image-create'),
  path('<int:pk>/update/', views.HeaderImageUpdateDelete.as_view(), name='header-image-update'),
  path('<int:pk>/delete/', views.HeaderImageUpdateDelete.as_view(), name='header-image-delete'),
  path('colors/', views.ColorList.as_view(), name='color-list'),
  path('categories/', views.CategoryList.as_view(), name='category-list'),
  path('sizes/', views.SizeList.as_view(), name='size-list'),
  path('products/', views.ProductList.as_view(), name='product-list'),
  path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
  path('product-images/', views.ProductImageList.as_view(), name='product-image-list'),
  path('SignUp/', views.signup, name='SignUp'),
  path('Login/', views.login_view, name='Login'),
  path('check-order-status/', views.CheckOrderStatus.as_view(), name='check_order_status'),
  path('update-order-status/', views.UpdateOrderStatus.as_view(), name='update_order_status'),
  path('api/laundry/', views.LaundryServiceList.as_view(), name='laundry-list'),
    path('api/laundry/<int:pk>/', views.LaundryServiceDetail.as_view(), name='laundry-detail'),
]

