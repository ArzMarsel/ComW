# Generated by Django 5.0.7 on 2024-07-10 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_zaiavka'),
    ]

    operations = [
        migrations.AddField(
            model_name='zaiavka',
            name='mark',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]