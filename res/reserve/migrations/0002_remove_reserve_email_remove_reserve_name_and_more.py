# Generated by Django 4.2 on 2023-05-25 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reserve', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserve',
            name='email',
        ),
        migrations.RemoveField(
            model_name='reserve',
            name='name',
        ),
        migrations.AddField(
            model_name='reserve',
            name='user',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reserve', to=settings.AUTH_USER_MODEL),
        ),
    ]