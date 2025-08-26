from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import PostDetailView, PostListView
# CRUD
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail'),
    # CRUD
    path('create/', PostCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)