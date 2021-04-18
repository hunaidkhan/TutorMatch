from django.urls import path
from user_form import views

urlpatterns = [
    path('', views.user_form, name='user_form'),
]