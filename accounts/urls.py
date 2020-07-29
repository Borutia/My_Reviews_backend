from django.urls import path, re_path
from accounts.views import Registration_API_View, Login_API_View

urlpatterns = [
    re_path(r'^registration/$', Registration_API_View.as_view(), name='user_registration'),
    re_path(r'^login/$', Login_API_View.as_view(), name='user_login'),
]

