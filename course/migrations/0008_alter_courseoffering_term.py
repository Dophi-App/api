# Generated by Django 4.1.1 on 2022-09-17 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_remove_lecture_course_lecture_offering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseoffering',
            name='term',
            field=models.CharField(choices=[('fall', 'fall'), ('winter', 'winter'), ('spring', 'spring'), ('summer', 'summer')], default='fall', max_length=10),
        ),
    ]
