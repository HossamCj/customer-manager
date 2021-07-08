from django.urls import path

from .views import *


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('customer/<int:id>/', customer_home, name='customer_home'),
    path('customer/settings/<int:id>/', customer_settings, name='customer_settings'),
    path('customer/settings/edited/', customer_settings_edited, name='customer_settings_edited'),

    path('client/<int:id>/', client, name='client'),

    path('signup-admin/', signup_admin, name='signup_admin'),
    path('signup-customer/', signup_customer, name='signup_customer'),

    path('login/', login_all, name='login_all'),
    path('logout/', logout_all, name='logout_all'),
]
