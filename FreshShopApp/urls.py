from django.urls import path
from . import views


urlpatterns=[
    path('login/',views.Login,name='login'),
    path('register/',views.user_registration,name='user_registration'),
    path('',views.view_products,name='products'),
    path('add-to-cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('view-cart/',views.view_cart,name='view_cart'),
    path('remove/<int:item_id>/',views.remove_cart,name='remove'),
    path('update-quantity/<int:product_id>/<str:action>/',views.update_quantity,name='update'),
    path('logout/',views.Logout,name='logout'),
    path('checkout/',views.checkout,name='checkout'),
    path('search/',views.search_product,name='search')
]