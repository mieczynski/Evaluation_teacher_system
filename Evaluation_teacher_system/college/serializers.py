from django.core.exceptions import ObjectDoesNotExist

from Evaluation_teacher_system.college.models import College
from rest_framework import serializers


class CreateCollegeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=128, required=True)
    city = serializers.CharField(required=True, max_length=128)

    class Meta:
        model = College
        fields = ['name', 'city']

    def create(self, validated_data):
        try:
            college = College.objects.get(name=validated_data['name'])
        except ObjectDoesNotExist:
            college = College.objects.create_college(validated_data['name'], validated_data['city'])
        return college


class ListCollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = []


    def list(self):
        try:
            colleges_list = College.objects.get_all_objects()
        except ObjectDoesNotExist:
            return []
        return colleges_list
