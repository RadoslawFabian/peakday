# Generated by Django 5.1.6 on 2025-03-10 20:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dietplanner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('calories', models.IntegerField()),
                ('protein', models.FloatField()),
                ('carbs', models.FloatField()),
                ('fat', models.FloatField()),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='mealplan',
            name='meal_name',
        ),
        migrations.AddField(
            model_name='mealplan',
            name='meal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dietplanner.meal'),
        ),
    ]
