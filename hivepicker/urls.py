from django.urls import path
from . import views

urlpatterns = [
    path('', views.comment_picker, name='comment-picker'),
    path('picker/', views.comment_picker, name='comment-picker')
]