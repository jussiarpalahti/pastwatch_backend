
from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, GroupViewSet, DataViewSet, TagViewSet, schema_view

router = routers.DefaultRouter(schema_title='My API')
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'data', DataViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('swagger', schema_view),
]
