from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('blogs/', views.PostListView.as_view(), name='post-list'),
    path('bloggers/', views.BloggerListView.as_view(), name='blogger-list')
]
