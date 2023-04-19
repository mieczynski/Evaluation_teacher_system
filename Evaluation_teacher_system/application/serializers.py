from django.core.exceptions import ObjectDoesNotExist

from Evaluation_teacher_system.application.models import Application
from rest_framework import serializers


class CreateApplicationSerializer(serializers.ModelSerializer):
    data = serializers.JSONField(required=True)
    type = serializers.IntegerField(required=True)

    class Meta:
        model = Application
        fields = ['data', 'type']

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request.user.is_authenticated:
            user_id = request.user.id
            college_id = request.user.college_id
        else:
            user_id = 0
            college_id = 0

        application = Application.objects.create_application(validated_data['data'], validated_data['type'], user_id, college_id)
        return application


class ListApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = []

    def list(self, filterType):
        try:
            if filterType:
                applications_list = Application.objects.getApplicationByFilter(filterType)
            else:
                applications_list = Application.objects.get_all_objects()

        except ObjectDoesNotExist:
            return []
        return applications_list


class UpdateApplicationSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=128, required=True)
    class Meta:
        model = Application
        fields = ['id']

    def confirm(self, validated_data):
        application = Application.objects.confirm(validated_data['id'])
        return application

    def delete(self, validated_data):
        application = Application.objects.delete(validated_data['id'])
        return application
