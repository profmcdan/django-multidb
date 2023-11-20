from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StudentViewSet

app_name = 'student'

router = DefaultRouter()
router.register('', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
