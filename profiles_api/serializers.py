from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from profiles_api.models import UserProfile


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = UserProfile
        fields = ("id", "email", "name", "password")
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {
                    "input_type": "password",
                },
            },
        }

    def create(self, validated_data):
        """Create and return a new user"""
        email, name, password = (
            validated_data["email"],
            validated_data["name"],
            validated_data["password"],
        )
        user = UserProfile.objects.create_user(email, name, password)

        return user

    def update(self, instance, validated_data):
        """Handles updating user account"""
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)

        return super().update(instance, validated_data)
