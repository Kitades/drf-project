from rest_framework.test import APITestCase, force_authenticate

from materials.models import Course, Lesson
from users.models import User


class LessonsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.course = Course.objects.create(title="test_course", description="test_description")
        self.lesson = Lesson.objects.create(title='test_lesson')
