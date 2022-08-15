from django.urls import include, re_path
from django.urls import path
from . import views
import Home_App
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Accounts_App'

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('login_user', views.login_user, name='login_user'),
    path('register', views.register, name='register'),
    path('logout_request', views.logout_request, name='logout'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('not_authorized', views.not_authorized, name='not_authorized'),
    path('profile_register/<int:id>', views.profile_register_view, name='profile_register_view'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

