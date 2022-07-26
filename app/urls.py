from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # routing untuk Admin
    path('admin/', admin.site.urls),
    path('api/', include('news.urls')),
]
