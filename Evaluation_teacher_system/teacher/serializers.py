from django.core.exceptions import ObjectDoesNotExist

from Evaluation_teacher_system.teacher.models import Teacher
from rest_framework import serializers


class CreateTeacherSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=128, required=True)
    last_name = serializers.CharField(max_length=128, required=True)
    teacher_id = serializers.CharField(max_length=6, required=True)
    collage = serializers.CharField(max_length=6, required=True)
    subject_id = serializers.CharField(max_length=6, required=True)

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'teacher_id', 'college', 'subject_id']

    def create(self, validated_data):
        try:
            teacher = Teacher.objects.get(teacher_id=validated_data['teacher_id'])
        except ObjectDoesNotExist:
            teacher = Teacher.objects.create_teacher(validated_data['first_name'], validated_data['last_name'],
                                                     validated_data['teacher_id'], validated_data['college'],
                                                     validated_data['subject_id'])
        return teacher


class ListTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = []

    def list(self):
        try:
            teachers_list = Teacher.objects.get_all_objects()
        except ObjectDoesNotExist:
            return []
        return teachers_list


class GetTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'rate_avg']
