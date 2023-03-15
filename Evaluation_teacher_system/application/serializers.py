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
        application = Application.objects.create_application(validated_data['data'], validated_data['type'])
        return application


# class ListCollegeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = College
#         fields = []
#
#
#     def list(self):
#         try:
#             colleges_list = College.objects.get_all_objects()
#         except ObjectDoesNotExist:
#             return []
#         return colleges_list
