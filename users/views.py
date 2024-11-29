from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from users.models import Payments
from users.serializers import PaymentsSerializer


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ('payment_type','payment_course', 'payment_lesson')
    ordering_fields = ('date_payment',)




