# Generated by Django 4.1.1 on 2022-09-17 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_alter_courseoffering_term'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseoffering',
            name='year',
        ),
        migrations.AlterField(
            model_name='courseoffering',
            name='term',
            field=models.CharField(default='mmmmyyyy', max_length=15),
        ),
    ]