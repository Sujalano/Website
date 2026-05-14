from django.contrib import admin
from django.urls import path
from ecom import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
  
    path('buildings',views.home_view,name=''),
    path('prebuild-website/afterlogin', views.afterlogin_view,name='afterlogin'),
    path('prebuild-website/logout', LogoutView.as_view(template_name='ecom/logout.html'),name='logout'),
    path('prebuild-website/aboutus', views.aboutus_view),
    path('prebuild-website/contactus', views.contactus_view,name='contactus'),
    path('prebuild-website/search', views.search_view,name='search'),
    path('prebuild-website/send-feedback', views.send_feedback_view,name='send-feedback'),
    path('prebuild-website/view-feedback', views.view_feedback_view,name='view-feedback'),

    path('prebuild-website/adminclick', views.adminclick_view),
    path('prebuild-website/adminlogin', LoginView.as_view(template_name='ecom/adminlogin.html'),name='adminlogin'),
    path('prebuild-website/admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('prebuild-website/view-customer', views.view_customer_view,name='view-customer'),
    path('prebuild-website/delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),
    path('prebuild-website/update-customer/<int:pk>', views.update_customer_view,name='update-customer'),

    path('prebuild-website/admin-products', views.admin_products_view,name='admin-products'),
    path('prebuild-website/admin-add-product', views.admin_add_product_view,name='admin-add-product'),
    path('prebuild-website/delete-product/<int:pk>', views.delete_product_view,name='delete-product'),
    path('prebuild-website/update-product/<int:pk>', views.update_product_view,name='update-product'),

    path('prebuild-website/admin-view-booking', views.admin_view_booking_view,name='admin-view-booking'),
    path('prebuild-website/delete-order/<int:pk>', views.delete_order_view,name='delete-order'),
    path('prebuild-website/update-order/<int:pk>', views.update_order_view,name='update-order'),


    path('prebuild-website/customersignup', views.customer_signup_view),
    path('prebuild-website/customerlogin', LoginView.as_view(template_name='ecom/customerlogin.html'),name='customerlogin'),
    path('prebuild-website/customer-home', views.customer_home_view,name='customer-home'),
    path('prebuild-website/my-order', views.my_order_view,name='my-order'),
    # path('my-order', views.my_order_view2,name='my-order'),
    path('prebuild-website/my-profile', views.my_profile_view,name='my-profile'),
    path('prebuild-website/edit-profile', views.edit_profile_view,name='edit-profile'),
    path('prebuild-website/download-invoice/<int:orderID>/<int:productID>', views.download_invoice_view,name='download-invoice'),


    path('prebuild-website/add-to-cart/<int:pk>', views.add_to_cart_view,name='add-to-cart'),
    path('prebuild-website/cart', views.cart_view,name='cart'),
    path('prebuild-website/remove-from-cart/<int:pk>', views.remove_from_cart_view,name='remove-from-cart'),
    path('prebuild-website/customer-address', views.customer_address_view,name='customer-address'),
    path('prebuild-website/payment-success', views.payment_success_view,name='payment-success'),


]
