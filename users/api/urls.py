from django.urls import path
from users.api.views import AccountView, UpdatePassowrdView, AccountUpdateView

app_name = 'users'

urlpatterns = [
    path('me', AccountView.as_view(), name='me'),
    path('update', AccountUpdateView.as_view(), name='update'),
    path('change-password', UpdatePassowrdView.as_view(), name='change-password')
]