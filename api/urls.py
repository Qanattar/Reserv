from . import views
from django.urls import path



urlpatterns = [
    path('main/', views.main, name='main'),
    path('hello_page/', views.hello_page, name='hello_page'),
    path('times/', views.times, name='times'),
    path('clients/', views.clients, name='clients'),
    path('client/<int:pk>', views.client_detail, name='client_detail'),
    path('', views.registration_page, name='registration_page'),
    path('create_record/<int:pk>', views.create_record, name='create_record'),
    path('delete_record/<int:pk>/', views.delete_record, name="delete_record"),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('send_email/<int:pk>', views.send_email, name='send_email'),

]
