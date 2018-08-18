from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('register/<id>/<pw>/<name>', views.register, name='register'),
    path('login/<id>/<pw>',views.login,name='login'),
]