import json

from django.forms import model_to_dict
from django.core import serializers

from django.db import models

from Evaluation_teacher_system.user.models import User
from Evaluation_teacher_system.teacher.models import Teacher


class RatingManager(models.Manager):

    def create_rating(self, points, comment, teacher_id, user_id):
        user = User.objects.get(id=user_id)
        teacher = Teacher.objects.get(id=teacher_id)
        rating = Rating(points=points, comment=comment, teacher=teacher,
                        user=user)
        rating.save(using=self._db)
        rating_list = Rating.objects.filter(teacher=teacher_id)
        points_sum = 0;
        for rating in rating_list:
            points_sum += rating.points

        rate_avg = points_sum / len(rating_list)
        teacher.rate_avg = rate_avg
        teacher.save(using=self._db)
        return rating

    def get_all_objects(self, teacher_id):
        queryset = list(Rating.objects.filter(teacher=teacher_id).values())
        data = []
        qs_json = serializers.serialize('json', Rating.objects.all())

        return queryset


class Rating(models.Model):
    comment = models.CharField(max_length=255)
    points = models.FloatField(max_length=2, default=0)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = RatingManager()

    def __str__(self):
        array = {
            "comment": self.comment,
            "points": self.points
        }
        return json.dumps(array)

    class Meta:
        db_table = 'rating'
