# Generated by Django 4.1.1 on 2022-09-17 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_school_abbreviation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='abbreviation',
            field=models.CharField(default='none', max_length=50),
        ),
    ]
