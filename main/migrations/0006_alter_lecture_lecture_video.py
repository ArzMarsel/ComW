# Generated by Django 5.0.6 on 2024-07-19 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_grade_assignment_grade_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='lecture_video',
            field=models.TextField(verbose_name='Video:'),
        ),
    ]
