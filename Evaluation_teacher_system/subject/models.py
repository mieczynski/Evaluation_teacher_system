from django.forms import model_to_dict

from django.db import models


class SubjectManager(models.Manager):

    def create_subject(self, name):
        subject = Subject(name=name)
        subject.save(using=self._db)
        return subject

    def get_all_objects(self):
        queryset = list(Subject.objects.all())

        data = []
        if isinstance(queryset, list):
            for subject in queryset:
                data.append({'subject': model_to_dict(subject)})
        else:
            data.append({'subject': model_to_dict(queryset)})

        return data


class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False)

    objects = SubjectManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subject'
