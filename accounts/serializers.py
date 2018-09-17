from django.contrib.auth.models import User
from rest_framework import serializers





class UserSerializer(serializers.ModelSerializer):
    """
    UserSerializer

    Handles the serialization of the `User` model.

    The fields to be serialized are:
    - username
    - password
    """

    class Meta:
        model = User
        fields = ('username', 'password')