from django.urls import path

from rest_framework.routers import SimpleRouter

from materials.views import CourseViewSet, LessonListAPIView, LessonRetrieveAPIView, LessonCreateAPIView, \
    LessonDestroyAPIView, LessonUpdateAPIView

from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register('', CourseViewSet)

urlpatterns = [
                  path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
                  path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-retrieve'),
                  path('lessons/create/', LessonCreateAPIView.as_view(), name='lessons-create'),
                  path('lessons/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
                  path('lessons/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson-update'),

              ] + router.urls
