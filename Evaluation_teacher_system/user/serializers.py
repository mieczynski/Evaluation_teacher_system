from Evaluation_teacher_system.user.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'collage', 'is_active']
        read_only_field = ['is_active']
