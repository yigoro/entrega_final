from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog_sab_app/', include('blog_sab_app.urls')),
]
