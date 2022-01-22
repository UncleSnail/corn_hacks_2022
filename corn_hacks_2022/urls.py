
from django.contrib import admin
from django.urls import include, path
from Screed import views


urlpatterns = [
    path('Screed/', include('Screed.urls')),
    path('admin/', admin.site.urls),
    path('private_place/', views.private_place),
    path('accounts/', include("django.contrib.auth.urls")),
]
