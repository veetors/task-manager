# Generated by Django 3.1.1 on 2020-10-10 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0002_auto_20201010_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskstatus',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
