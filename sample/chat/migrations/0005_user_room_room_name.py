# Generated by Django 4.1.7 on 2023-03-04 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_user_room_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_room',
            name='room_name',
            field=models.CharField(default='gg', max_length=100),
        ),
    ]
