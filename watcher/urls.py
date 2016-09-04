
from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, GroupViewSet, schema_view

router = routers.DefaultRouter(schema_title='My API')
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('swagger', schema_view),
]
