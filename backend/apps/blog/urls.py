from django.urls import path
from .views import *

urlpatterns = [
    path('post-list/', PostListCreateAPIView.as_view()),
    path('post-detail/<int:pk>/', PostRetrieveAPIView.as_view()),
    path('post-destroy/<int:pk>/', PostDestroyAPIView.as_view()),
]