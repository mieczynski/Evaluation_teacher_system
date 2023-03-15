
import json

from django.forms import model_to_dict

from django.db import models


class ApplicationManager(models.Manager):

    def create_application(self,  data, type):
        application = Application(data=data, type=type, status=0)
        application.save(using=self._db)
        return application

    # def get_all_objects(self):
    #     queryset = list(College.objects.all())
    #     data = []
    #     if isinstance(queryset, list):
    #         for college in queryset:
    #             data.append({'college': model_to_dict(college)})
    #     else:
    #         data.append({'college': model_to_dict(queryset)})
    #
    #     return data


class Application(models.Model):
    type = models.IntegerField()
    status = models.IntegerField()
    data = models.CharField(max_length=250)

    objects = ApplicationManager()

    def __str__(self):
        array = {
            "name": self.status,
            "city": self.type
        }
        return json.dumps(array)

    class Meta:
        db_table = 'application'
