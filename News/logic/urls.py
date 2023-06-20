from django.urls import path
from .views import  ( index,news_details,create_news_post, update_news_post,delete_news_post )

urlpatterns = [
    path('', index, name="home"),
    path('news/<int:pk>', news_details, name="news-detail"),
    path('write', create_news_post, name="create-news-post" ),
    path('news/update/<int:pk>', update_news_post, name="update-news-post"),
    path('news/delete/<int:pk>', delete_news_post, name="delete-news-post")
    ]