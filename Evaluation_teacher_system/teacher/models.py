import json

from django.core import serializers
from django.db import models
from django.forms import model_to_dict

from Evaluation_teacher_system.subject.models import Subject
from Evaluation_teacher_system.college.models import College


class TeacherManager(models.Manager):

    def create_teacher(self, first_name, last_name,  college_id, subject_id):
        collage = College.objects.get(id=college_id)
        subject = Subject.objects.get(id=subject_id)
        teacher = Teacher(first_name=first_name, last_name=last_name, collage=collage)
        teacher.save(using=self._db)
        teacher.subject_id.add(subject)

        return teacher

    def get_all_objects(self):
        queryset = list(Teacher.objects.all().values())
        if isinstance(queryset, list):
            for teacher in queryset:
                subjects = Subject.objects.filter(teacher=teacher['id'])
                teacher['subjects'] = subjects.values('name')

        return queryset

    def getTeacher(self, teacher_id):
        queryset = list(Teacher.objects.filter(teacher_id=teacher_id).values())
        if isinstance(queryset, list):
            for teacher in queryset:
                subjects = Subject.objects.filter(teacher=teacher['id'])
                teacher['subjects'] = subjects.values('name')

        return queryset

    def getTeacherByFilter(self, filter, filterType):
        queryset = '';
        if filterType == 'first_name' and filter:
            queryset = list(Teacher.objects.filter(first_name__contains=filter).values())
        elif filterType == 'last_name' and filter:
            queryset = list(Teacher.objects.filter(last_name__contains=filter).values())
        elif filterType == 'subject' and filter:
            queryset = list(Teacher.objects.filter(subject_id__name__contains=filter).values())
        if isinstance(queryset, list):
            for teacher in queryset:
                subjects = Subject.objects.filter(teacher=teacher['id'])
                teacher['subjects'] = subjects.values('name')

        return queryset




class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    rate_avg = models.FloatField(max_length=2, default=0)
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=False)
    subject_id = models.ManyToManyField(Subject)

    objects = TeacherManager()

    def __str__(self):
        array = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "rate_avg": self.rate_avg,
            'college_id': self.college_id,
        }
        return json.dumps(array)

    class Meta:
        db_table = 'teacher'
