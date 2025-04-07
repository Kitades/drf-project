from rest_framework.serializers import ModelSerializer, SerializerMethodField

from users.models import Payments, User, Follow, Donation


class PaymentsSerializer(ModelSerializer):
    # def get_date_payment(self):
    class Meta:
        model = Payments
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class FollowSerializer(ModelSerializer):
    follow_check = SerializerMethodField()

    def get_follow_check(self, instance):
        if instance.follow_courses.all().first():
            return instance.follow_courses.all().first().course
        return 0

    class Meta:
        model = Follow
        fields = "__all__"


class DonationSerializer(ModelSerializer):
    class Meta:
        model = Donation
        fields = "__all__"
