from django.contrib import admin
from django.urls import path, include
from users.views import register
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('django.contrib.auth.urls')),
    path('cadastro/', register, name='register'),
    path('workouts/', include('workouts.urls')),
    path('users/', include('users.urls')),
    path('', include('core.urls')),
    #    path('workouts/', include('workouts.urls')),
    #  path('users/', include('users.urls')),
]

handler404 = 'core.views.handler404'
handler500 = 'core.views.handler500'
