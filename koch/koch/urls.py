from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

import playgrounds.views
from django.conf.urls import (handler404, handler500)


handler404 = 'playgrounds.views.handler404'
handler500 = 'playgrounds.views.handler500'

app_name = 'accounts'
urlpatterns = [
    path('', include('social_django.urls')),
    path('admin/', admin.site.urls),
    path('logout/', playgrounds.views.logout_view, name='logout'),
    path('', playgrounds.views.index),
    path('b', playgrounds.views.basketball),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
