# Generated by Django 4.2 on 2023-05-20 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0009_fooddislike'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fooddislike',
            old_name='Dislikefood',
            new_name='dislikefood',
        ),
        migrations.RenameField(
            model_name='fooddislike',
            old_name='Dislikeuser',
            new_name='dislikeuser',
        ),
    ]
