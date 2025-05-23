from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_user

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login_user'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_user'),
    path('register/', register_user, name='register_user'),  # ← TO ROZWIĄZUJE TWÓJ BŁĄD
]
