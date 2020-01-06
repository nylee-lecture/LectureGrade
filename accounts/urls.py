from django.contrib.auth import views as auth_view
from django.urls import path
from accounts.views import register, profile, login


urlpatterns = [
    # path('login/', auth_view.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('login/', login, name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name = 'profile'),

]