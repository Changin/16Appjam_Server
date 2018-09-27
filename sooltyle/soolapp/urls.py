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
router.register('tips',soolapp.api.TipViewSet)

urlpatterns = [
	path('rest-auth/',include('rest_auth.urls')),
 	path('rest-auth/registration',include('rest_auth.registration.urls')),
 	path('users/', include('users.urls')),
    path('doc/',get_swagger_view(title='Rest API Document')),
    path('board/',include((router.urls, app_name),namespace='api')),
]