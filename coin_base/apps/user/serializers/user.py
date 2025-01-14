from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(ModelSerializer):
    """Serializer for user objects."""
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        """Meta Option."""
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate(self, attrs):
        """Validate Option."""
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError({"confirm_password": "The passwords don't match."})
        attrs.pop('confirm_password', None)
        return attrs


class UserPasswordSerializer(serializers.Serializer):
    """Serializer for user password."""
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    current_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        """Validate Option."""
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError({"confirm_password": "The passwords don't match."})
        return attrs
