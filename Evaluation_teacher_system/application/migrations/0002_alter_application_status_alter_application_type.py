# Generated by Django 4.1.3 on 2023-03-15 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='application',
            name='type',
            field=models.IntegerField(),
        ),
    ]