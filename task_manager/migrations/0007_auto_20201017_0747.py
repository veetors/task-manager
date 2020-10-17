# Generated by Django 3.1.1 on 2020-10-17 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0006_auto_20201013_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(to='task_manager.Tag'),
        ),
    ]
