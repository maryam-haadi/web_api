
from django.urls import path
from foods import views

app_name='foods'

urlpatterns=[
    path("food_list",views.food_list,name='food_list'),
    path("food_slider",views.food_slider,name='food_slider'),
    path("food_detail/<f_id>",views.food_detail,name='food_detail'),
    path("send_comment/<f_id>",views.send_comment,name='send_comment'),
    path("breakfast",views.breakfast,name='breakfast'),
    path("dinner",views.dinner,name='dinner'),
    path("lunch",views.lunch,name='lunch'),
    path("drink",views.drink,name='drink'),
    path("delete/<c_id>",views.delete_comment,name='delete_comment'),
    path("show_comment/<f_id>",views.show_comment,name='show_comment'),
    path("search",views.FoodsAPIView.as_view(),name='search'),
    path("like/<f_id>",views.like,name='like'),
    path("dislike/<f_id>",views.dislike,name='dislike'),
]
