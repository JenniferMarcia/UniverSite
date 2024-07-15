from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "last_name",
            "first_name",
            "phone_number",
            "adress",
            "type_user",
            "password",
            "email",
            "profil_picture",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = CustomUser.objects.create(
            **validated_data,
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
