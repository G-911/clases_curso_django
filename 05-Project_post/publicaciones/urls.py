from django.urls import path

from .views import PostDetailView, PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail')
]