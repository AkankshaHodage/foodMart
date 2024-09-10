
from django.urls import path, include
from . import views

urlpatterns = [
    path('registerUser/',views.registerUser,name='registerUser'),
    path('registerRestaurant/',views.registerRestaurant,name='registerRestaurant'),
    path('login/',views.login,name='login'),
    path('myAccount/',views.myAccount,name='myAccount'),
    path('logout/',views.logout,name='logout'),
    path('RestaurantDashboard/',views.RestaurantDashboard,name='RestaurantDashboard'),
    path('custDashboard/',views.custDashboard,name='custDashboard'),





]
