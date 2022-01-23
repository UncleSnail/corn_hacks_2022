
from django.contrib import admin
from django.urls import path, include
from Screed import views as Screed_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', Screed_views.index, name='index'),
    path('Screed/', include('Screed.urls')),
    path('account/', include('users_app.urls')),
    
    # path('accounts/', include("django.contrib.auth.urls")),
   

]
