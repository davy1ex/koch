from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from main import views
from django.conf.urls import ( handler404, handler500
)

from main.views import PlaygroundView


handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.index),
    path('main/b', PlaygroundView.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
