from django.urls import path
from IntegritasTecnica.apps.users.api.view import UserListAPIView

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
]
