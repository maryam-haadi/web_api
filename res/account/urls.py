from django.urls import path
from account import views




app_name='account'

urlpatterns=[

    path("register",views.Register,name='Register'),
    path("user_list",views.user_list,name='user_list'),
    path("login_user",views.login_user,name='login_user'),
    path("logout_user",views.logout_user,name='logout_user'),
    
]







