# Generated by Django 5.1.6 on 2025-05-15 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_budget_created_at_alter_budget_monthly_income'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
