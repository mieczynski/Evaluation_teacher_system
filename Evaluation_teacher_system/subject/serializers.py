from django.core.exceptions import ObjectDoesNotExist

from Evaluation_teacher_system.subject.models import Subject
from rest_framework import serializers


class CreateSubjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=128, required=True)

    class Meta:
        model = Subject
        fields = ['name']

    def create(self, validated_data):
        try:
            subject = Subject.objects.get(name=validated_data['name'])
        except ObjectDoesNotExist:
            subject = Subject.objects.create_subject(validated_data['name'])
        return subject


class ListSubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = []

    def list(self):
        try:
            subjects_list = Subject.objects.get_all_objects()
        except ObjectDoesNotExist:
            return []
        return subjects_list



