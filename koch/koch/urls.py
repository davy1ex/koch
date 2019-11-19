from django.contrib import admin
from django.urls import path

from main import views
from django.conf.urls import ( handler404, handler500
)


handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('main/', views.index),
    # path('/404', views.handler404)
]
