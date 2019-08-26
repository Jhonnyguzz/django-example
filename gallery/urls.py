from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    #url(r'^ind$/', views.index, name='index')}
    path('', views.index, name='index'),
    path('add/', views.add_image, name='addImage')
]
