from django.contrib import admin
from django.urls import path, include

from .views import (
    sing_in, sing_up, log_out,
    forgot_password, update_password, 
    list_user, user_state, set_profil,get_role,
)
urlpatterns = [
    #path('', dashboard, name='dashboard'),
    path('login', sing_in, name='sing_in'),
    path('register', sing_up, name='sing_up'),
    path('logout', log_out, name='log_out'),
    path('forgot-password', forgot_password, name='forgot_password'),
    path('update-password', update_password, name='update_password'),

    path("user_list", list_user, name='user_list'),
    path("user_state", user_state, name='user_state'),
    path("set_profil", set_profil, name='set_profil'),
    path("get_role/<int:user_id>", get_role, name='get_role'),
]