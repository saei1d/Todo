# Generated by Django 4.2.1 on 2023-06-01 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
