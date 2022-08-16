from django.urls import include, re_path
from django.urls import path
from . import views
import Home_App
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Admin_App'

urlpatterns = [
    path('', views.admin_panel, name='admin_panel'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('logout_request', views.logout_request, name='logout'),
    path('main_category', views.main_category, name='main_category'),
    path('sub_category', views.sub_category, name='sub_category'),
    path('user_grid', views.user_grid, name='user_grid'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)