from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet

app_name = 'teacher'

router = DefaultRouter()
router.register('', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
