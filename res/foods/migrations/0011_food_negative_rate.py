# Generated by Django 4.2 on 2023-05-25 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0010_rename_dislikefood_fooddislike_dislikefood_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='negative_rate',
            field=models.IntegerField(default=0),
        ),
    ]
