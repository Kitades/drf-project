from rest_framework.serializers import ModelSerializer, SerializerMethodField

from users.models import Payments, User


class PaymentsSerializer(ModelSerializer):

    # def get_date_payment(self):
    #     ret
    class Meta:
        model = Payments
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
