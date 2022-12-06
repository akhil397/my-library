from django.urls import path
from cartpage import views
urlpatterns = [
    path('cartDetails', views.cart_details, name='cartDetails'),
    path('add/<int:product_id>/', views.add_cart, name='addcart'),
   
    path('update-item',views.updateItem ,name='update-item'),

    path('checkout',views.checkout,name='checkout'),

    path('despach/',views.processOrder ,name='processOrder'),



]