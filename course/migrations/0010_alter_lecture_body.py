# Generated by Django 4.1.1 on 2022-09-17 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_remove_courseoffering_year_alter_courseoffering_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='body',
            field=models.TextField(null=True),
        ),
    ]
