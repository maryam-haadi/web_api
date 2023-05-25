# Generated by Django 4.2 on 2023-05-20 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foods', '0007_foodlike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodlike',
            name='likeuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]