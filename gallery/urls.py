from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    #url(r'^ind$/', views.index, name='index')}
    path('', views.index, name='index'),
    path('add/', views.add_image, name='addImage'),
    path('view', views.view_images, name='view_images'),
    path('new', views.add_images_view, name='add_images_view'),
    path('addUser', views.add_user, name='addUser'),
    path('newUser', views.add_user_view, name='newUser')

]
