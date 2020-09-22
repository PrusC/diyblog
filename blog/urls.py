from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
]
