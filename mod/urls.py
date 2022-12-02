from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     # path('<str:room_name>/', views.room, name='room'),
     path('upload/', views.upload, name='upload'),
     path('detail/<int:media_id>/', views.detail, name='detail'),
]
