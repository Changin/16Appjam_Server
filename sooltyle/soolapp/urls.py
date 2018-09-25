from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from . import views
import soolapp.api

app_name = 'soolapp'

router = routers.DefaultRouter()
router.register('soolgames', soolapp.api.SoolGameViewSet)
router.register('recipes', soolapp.api.RecipesViewSet)

urlpatterns = [
    path('register/<id>/<pw>/<name>', views.register, name='register'),
    path('login/<id>/<pw>',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('api/doc/',get_swagger_view(title='Rest API Document')),
    path('api/',include((router.urls, app_name),namespace='api')),
]