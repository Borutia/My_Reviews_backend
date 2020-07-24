from django.urls import path
from accounts import views
#from django.contrib.auth import views

urlpatterns = [
    path(r'^sign_in/', views.sign_up),
    path(r'^sign_up/', views.sign_in),
    path(r'^my_account/', views.my_account),
]

