from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('user_login/',views.user_login, name='user_login'),
    path('home/',views.home, name='home'),
    path('basic_setting/',views.basic_setting, name='basic_setting'),
    path('article_detail/<int:article_id>/',views.article_detail, name='article_detail'),
    path('article_edit/<int:article_id>/',views.article_edit, name='article_edit'),
    path('article_submit/',views.article_submit, name='article_submit'),
    path('search/',views.search, name='search'),
    path('article_delete/<int:article_id>/',views.article_delete, name='article_delete')
]
app_name='myblog'