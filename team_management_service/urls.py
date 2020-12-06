from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

from members.views import TeamMemberViewSet

router = routers.SimpleRouter()
router.register('team-members', TeamMemberViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
