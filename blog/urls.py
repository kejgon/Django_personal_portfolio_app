
from django.urls import path

from  . import views

app_name = 'blog'

urlpatterns = [
    path('', views.All_blogs, name='blogs'),
    path('<int:blog_id>/', views.Detail, name='detail'),
]

