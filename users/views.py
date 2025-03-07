from rest_framework import filters
from rest_framework.generics import CreateAPIView, UpdateAPIView, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from materials.models import Course
from users.models import Payments, User, Follow
from users.serializers import PaymentsSerializer, UserSerializer, FollowSerializer


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ('payment_type', 'payment_course', 'payment_lesson')
    ordering_fields = ('date_payment',)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class FollowUpdateAPIView(UpdateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def post(self, *args, **kwargs):
        user = self.requests.user
        course_id = self.requests.data.get("id")
        course_item = get_object_or_404(Course, course_id)

        subs_item = Follow.objects.filter(user=user, course=course_item)

        # Если подписка у пользователя на этот курс есть - удаляем ее
        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'
        # Если подписки у пользователя на этот курс нет - создаем ее
        else:
            subs_item.create()
            message = 'подписка добавлена'
        # Возвращаем ответ в API
        return Response({"message": message})
