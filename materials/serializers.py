from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import validate_not_forbidden


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)
    link = serializers.URLField(validators=[validate_not_forbidden])

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')

    def get_count_lessons(self, object):
        return object.lesson_set.count()

    class Meta:
        model = Course
        fields = ('title', 'description', 'count_lessons', 'lessons')
