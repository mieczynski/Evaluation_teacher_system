import json
from json import JSONEncoder

from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict

from django.db import models

from Evaluation_teacher_system.college.models import CollegeManager, College
from Evaluation_teacher_system.subject.models import Subject, SubjectManager
from Evaluation_teacher_system.teacher.models import Teacher
from Evaluation_teacher_system.user.models import User


class ApplicationManager(models.Manager):
    new_status = 0
    confirm_status = 1
    deleted_status = 2
    teacher_type = 1
    college_type = 2

    def create_application(self, data, type, user_id, college_id):
        if college_id:
            college = College.objects.get(id=college_id)
            json_obj = json.loads(data)
            json_obj['college_name'] = college.name
            data = json.dumps(json_obj)
            # json_obj.replace('\'', '\"' )
        application = Application(data=data, type=type, status=0, user_id=user_id)
        application.save(using=self._db)
        return application

    def get_all_objects(self):
        queryset = list(Application.objects.filter(status=0))
        data = []
        if isinstance(queryset, list):
            for application in queryset:
                data.append({'application': model_to_dict(application)})
        else:
            data.append({'application': model_to_dict(queryset)})

        return data

    def getApplicationByFilter(self, filterType):
        queryset = '';
        if filterType == 'college':
            queryset = list(Application.objects.filter(type__contains=self.college_type, status=0).values())
        elif filterType == 'teacher':
            queryset = list(Application.objects.filter(type__contains=self.teacher_type, status=0).values())

        return queryset

    def confirm(self, id):
        try:
            application = Application.objects.get(id=id, status=self.new_status)
        except Application.DoesNotExist:
            application = None
        if application:
            data = json.loads(application.data)
            if application.type == self.teacher_type and application.user_id:
                first_name = data['first_name']
                last_name = data['last_name']
                subjects = data['subjects']
                college_id = User.objects.get(id=application.user_id).college_id
                teacher = Teacher(first_name=first_name, last_name=last_name, rate_avg=0, college_id=college_id)
                teacher.save(using=self._db)
                for subject in subjects:
                    subject_obj = SubjectManager.check_if_exist(self, subject)
                    teacher.subject_id.add(subject_obj)
                # teacher.save(using=self._db)
            elif application.type == self.college_type:
                name = data['name']
                city = data['city']
                college = CollegeManager.check_if_exist(self, name, city)
            application.status = self.confirm_status
            application.save(using=self._db)
            return model_to_dict(application)
        else:
            return None

    def delete(self, id):
        try:
            application = Application.objects.get(id=id, status=self.new_status)
        except Application.DoesNotExist:
            application = None
        if application:
            application.status = self.deleted_status
            application.save(using=self._db)
            return model_to_dict(application)
        else:
            return None


class Application(models.Model):
    type = models.IntegerField()
    status = models.IntegerField()
    user_id = models.IntegerField()
    data = models.CharField(max_length=250)

    objects = ApplicationManager()

    def __str__(self):
        array = {
            "status": self.status,
            "type": self.type
        }
        return json.dumps(array)

    class Meta:
        db_table = 'application'
