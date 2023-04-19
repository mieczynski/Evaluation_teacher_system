from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login

from Evaluation_teacher_system.user.serializers import UserSerializer
from Evaluation_teacher_system.user.models import User


class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['admin'] = user.is_superuser

        # ...
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data

class LogoutSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        # data['username'] = UserSerializer(self.user).data['username']
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data



class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    email = serializers.EmailField(required=True, write_only=True, max_length=128)
    college_id = serializers.IntegerField(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'college_id']

    def create(self, validated_data):
        try:
            user = User.objects.get(username=validated_data['username'])
        except ObjectDoesNotExist:
            user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                            validated_data['password'], validated_data['college_id'])
        return user
class ChangeUserPaswordSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    new_password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    class Meta:
        model = User
        fields = ['password', 'new_password']

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request.user.is_authenticated:
            user = request.user
            if user.check_password(validated_data['password']):
                user.set_password(validated_data['new_password'])
                user.save()
                return user
            else:
                return []


