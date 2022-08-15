from django.urls import include, re_path
from django.contrib import admin
from django.urls import include, path
from django.conf import settings 
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('babyline_admin/', include('Admin_App.urls')),
    path('', include('Home_App.urls')),
    path('accounts/', include('Accounts_App.urls')),
    path('admin/clearcache/', include('clearcache.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
