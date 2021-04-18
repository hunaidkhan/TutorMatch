from django.urls import path
from login_page import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
]