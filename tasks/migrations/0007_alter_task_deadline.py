# Generated by Django 5.1.6 on 2025-03-04 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_task_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
