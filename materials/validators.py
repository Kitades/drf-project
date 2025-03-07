from rest_framework.serializers import ValidationError

not_forbidden = ["https://www.youtube.com/"]

def validate_not_forbidden(value):
    if value not in not_forbidden:
        raise ValidationError("запрещеный URL.")

