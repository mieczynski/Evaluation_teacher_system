# Generated by Django 4.1.3 on 2022-12-23 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('points', models.FloatField(default=0, max_length=2)),
            ],
            options={
                'db_table': 'rating',
            },
        ),
    ]