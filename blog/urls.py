from django.contrib import admin
from django.urls import path
from . import views
#blogproject\blog\urls.py
urlpatterns = [
    path('<int:blog_id>',views.detail, name="detail"),
    path('create/', views.create, name="create"), #함수도 부를수 있다. 굳이 html만 부르는건 아니다.
    path('edit/<int:blog_id>', views.edit, name="edit"),
    path('delete/<int:blog_id>', views.delete, name="delete"),

    path('comment_add/<int:blog_id>', views.comment_add, name='comment_add'),
    path('comment_edit/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('comment_delete/<int:comment_id>', views.comment_delete, name='comment_delete'),
]