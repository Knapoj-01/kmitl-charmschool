# Generated by Django 3.2.5 on 2021-07-11 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210711_2008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['group_ref', 'student_id']},
        ),
    ]
