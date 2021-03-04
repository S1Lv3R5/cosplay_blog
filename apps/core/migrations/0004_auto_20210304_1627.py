# Generated by Django 3.1.6 on 2021-03-04 11:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_auto_20210304_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='models',
            name='stars_count',
        ),
        migrations.AddField(
            model_name='models',
            name='stars',
            field=models.ManyToManyField(related_name='stars', to=settings.AUTH_USER_MODEL),
        ),
    ]
