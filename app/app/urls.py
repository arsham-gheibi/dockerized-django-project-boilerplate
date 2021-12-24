from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static


def handler_404(request, exception):
    return redirect('store:home')


handler404 = 'app.urls.handler_404'


urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
