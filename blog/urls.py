from django.urls import path
from . import views

urlpatterns = [
#이부분을 채운다.
    path('<int:pk>/', views.single_post_page),
    path('', views.index),

]