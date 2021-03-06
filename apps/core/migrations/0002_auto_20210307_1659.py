# Generated by Django 3.1.6 on 2021-03-07 11:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
        migrations.AddField(
            model_name='image',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='images_liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cosplaypost',
            name='rubric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='core.cosplayrubric'),
        ),
        migrations.AlterField(
            model_name='cosplaypost',
            name='title',
            field=models.CharField(blank=True, max_length=70, validators=[django.core.validators.MinLengthValidator(45, message='Length has to be a minimum 45')], verbose_name='Наименование поста'),
        ),
        migrations.AlterField(
            model_name='models',
            name='stars',
            field=models.ManyToManyField(related_name='models', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ImageComment',
        ),
    ]
