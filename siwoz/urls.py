from django.contrib import admin
from django.urls import path
from django.urls import include
from web_registry.urls import *
from django.contrib.auth import views as auth_views
from users import views as u_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', u_views.logout_view, name='logout'),
    path('signup/', u_views.signup_view, name='signup'),
    path('admin/', admin.site.urls),
    path('', include('web_registry.urls')),
]
