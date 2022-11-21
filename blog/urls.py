from django.urls import path

from . import views

urlpatterns = [
    path('<slug:slug>/<int:pk>/', views.PostDetailView.as_view(), name='post_single'),
    path('post/', views.PostListView.as_view(), name='post_list'),
    path('', views.home),
]
