# Generated by Django 4.1.7 on 2023-03-04 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_user_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_room',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.room'),
        ),
    ]