from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

import playgrounds.views
from django.conf.urls import ( handler404, handler500
)

from playgrounds.views import PlaygroundView


handler404 = 'playgrounds.views.handler404'
handler500 = 'playgrounds.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', playgrounds.views.index),
    path('b', playgrounds.views.basketball),#PlaygroundView.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
