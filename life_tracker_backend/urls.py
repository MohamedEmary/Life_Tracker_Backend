from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .swagger import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("tracker.urls")),
    path("api/users/", include("users.urls")),
    path("api/collections/", include("pages.urls")),
    path("api/notifications/", include("notifications.urls")),
    path("api/tasks/", include("tasks.urls")),
    path("api/chat/", include("Chat.urls")),
]

# Add Swagger URL patterns
urlpatterns += swagger_urlpatterns

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
