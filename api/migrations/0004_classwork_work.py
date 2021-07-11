# Generated by Django 3.2.5 on 2021-07-11 18:33

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_student_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='classwork',
            name='work',
            field=models.FileField(null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='classwork/<django.db.models.fields.related.OneToOneField>'),
        ),
    ]