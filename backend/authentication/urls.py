from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


<<<<<<< HEAD
=======
app_name = 'authentication'

>>>>>>> add_viewsets
router = DefaultRouter()
router.register(r'support_entity_types', views.SupportEntityTypeViewSet)
router.register(r'supports', views.SupportViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'user_resources', views.UserResourceViewSet)
router.register(r'user_tasks', views.UserTaskViewSet)
router.register(r'user_topics', views.UserTopicViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
