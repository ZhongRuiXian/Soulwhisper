"""
Community 模块的URL配置
"""
from django.urls import path
from . import views

urlpatterns = [
    path('public/', views.public_diaries_view, name='public_diaries'),
    path('comment/', views.comment_view, name='comment'),
    path('like/', views.like_view, name='like'),
    path('follow/', views.follow_view, name='follow'),
    path('user/<int:user_id>/followers/', views.user_followers_view, name='user_followers'),
    path('user/<int:user_id>/following/', views.user_following_view, name='user_following'),
] 