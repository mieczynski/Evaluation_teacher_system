
import json

from django.forms import model_to_dict

from django.db import models


class CollegeManager(models.Manager):

    def create_college(self, name, city):
        college = College(city=city, name=name)
        college.save(using=self._db)
        return college

    def get_all_objects(self):
        queryset = list(College.objects.all())
        data = []
        if isinstance(queryset, list):
            for college in queryset:
                data.append({'college': model_to_dict(college)})
        else:
            data.append({'college': model_to_dict(queryset)})

        return data


class College(models.Model):
    city = models.CharField(max_length=255)
    name = models.CharField(max_length=255, unique=True)

    objects = CollegeManager()

    def __str__(self):
        array = {
            "name": self.name,
            "city": self.city
        }
        return json.dumps(array)

    class Meta:
        db_table = 'college'
