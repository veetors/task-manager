# Generated by Django 3.1.1 on 2020-10-10 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0003_auto_20201010_1155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='descriptions',
            new_name='description',
        ),
    ]