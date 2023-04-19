
from django.urls import path
from reserve import views


app_name='reserve'

urlpatterns=[
    path("reserve",views.reserve,name='reserve'),
    path("reserve_list",views.reserve_list,name='reserve_list'),
]












