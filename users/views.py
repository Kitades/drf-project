from rest_framework import filters, status
from rest_framework.generics import CreateAPIView, UpdateAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from materials.models import Course
from users.models import Payments, User, Follow
from users.serializers import PaymentsSerializer, UserSerializer, FollowSerializer, DonationSerializer
from users.services import convert_rub_to_usd, create_stripe_session, create_stripe_price, create_stripe_product


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ("payment_type", "payment_course", "payment_lesson")
    ordering_fields = ("date_payment",)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class FollowUpdateAPIView(UpdateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("id")
        course_item = get_object_or_404(Course, id=course_id)

        subs_item = Follow.objects.filter(user=user, courses=course_item)

        # Если подписка у пользователя на этот курс есть - удаляем ее
        if subs_item.exists():
            subs_item.delete()
            message = "подписка удалена"
            status_code = status.HTTP_200_OK
        # Если подписки у пользователя на этот курс нет - создаем ее
        else:
            subs_item.create()
            message = "подписка добавлена"
            status_code = status.HTTP_201_CREATED

        # Возвращаем ответ в API
        return Response({"message": message}, status=status_code)


class DonationCreateAPIView(CreateAPIView):
    serializer_class = DonationSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        course = Course.objects.get(pk=int(self.request.data.get('course')))
        payment = serializer.save(user=self.request.user)
        amount_in_dollars = convert_rub_to_usd(payment.amount)
        product = create_stripe_product(course)
        price = create_stripe_price(amount_in_dollars, product)
        session_id, payment_link = create_stripe_session(price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()
