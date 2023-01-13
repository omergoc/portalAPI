from django.urls import path
from users.api.views import AccountView, UpdatePassowrdView

app_name = 'users'

urlpatterns = [
    path('me', AccountView.as_view(), name='me'),
    path('change-password', UpdatePassowrdView.as_view(), name='change-password')
]