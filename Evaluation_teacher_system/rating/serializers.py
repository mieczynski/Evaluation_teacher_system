from django.core.exceptions import ObjectDoesNotExist

from Evaluation_teacher_system.rating.models import Rating
from rest_framework import serializers


class CreateRatingSerializer(serializers.ModelSerializer):
    points = serializers.CharField(max_length=128, required=True)
    comment = serializers.CharField(max_length=128, required=True)
    teacher_id = serializers.CharField(max_length=6, required=True)

    class Meta:
        model = Rating
        fields = ['points', 'comment', 'teacher_id']

    def create(self, validated_data):
        request = self.context.get('request', None)
        rating = Rating.objects.create_rating(validated_data['points'], validated_data['comment'],
                                              validated_data['teacher_id'], request.user.id)
        return rating


class ListRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = []

    def list(self, teacher_id):
        try:
            ratings_list = Rating.objects.get_all_objects(teacher_id)
        except ObjectDoesNotExist:
            return []
        return ratings_list
