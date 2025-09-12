from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import PostDetailView, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("detail/<int:pk>", PostDetailView.as_view(), name="detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
