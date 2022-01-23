
from django.contrib import admin
from django.urls import path, include
from Screed import views as Screed_views


urlpatterns = [
    path('Screed/', include('Screed.urls')),
    path('admin/', admin.site.urls),
    # path('private_place/', views.private_place),
    # path('accounts/', include("django.contrib.auth.urls")),
    # path('add_messages/',views.add_messages),

]
