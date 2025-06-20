from django.urls import path
from .views import RegisterView, LoginView, LogoutView, MeView, PasswordUpdateView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('me/', MeView.as_view()),
    path('password-update/', PasswordUpdateView.as_view(), name='password-update'),
]
