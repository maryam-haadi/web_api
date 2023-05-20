# Generated by Django 4.2 on 2023-05-20 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foods', '0006_alter_comment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likefood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='foods.food')),
                ('likeuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
