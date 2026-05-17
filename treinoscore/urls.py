# urls.py Principal
from django.contrib import admin
from django.urls import path, include
from users.views import register
from rest_framework.authtoken.views import obtain_auth_token
from workouts.viewsets import CustomTokenLoginView

urlpatterns = [
    path('adminsep_pl/', admin.site.urls),
    path('contas/', include('django.contrib.auth.urls')),
    path('cadastro/', register, name='register'),

    path('workouts/', include('workouts.urls')),
    path('users/', include('users.urls')),
    path('', include('core.urls')),

    # Rotas da API
    path('api/v1/', include('workouts.api_urls')),
    path('api/v1/login/', CustomTokenLoginView.as_view(),
         name='api_token_auth'),  # <- APENAS ESTA
    path('api-auth/', include('rest_framework.urls')),

]
handler404 = 'core.views.handler404'
handler500 = 'core.views.handler500'
