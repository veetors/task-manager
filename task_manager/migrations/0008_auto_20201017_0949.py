# Generated by Django 3.1.1 on 2020-10-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0007_auto_20201017_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(null=True, to='task_manager.Tag'),
        ),
    ]
