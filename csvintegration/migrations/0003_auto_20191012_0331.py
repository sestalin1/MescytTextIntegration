# Generated by Django 2.2.6 on 2019-10-12 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csvintegration', '0002_auto_20191011_2317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carreer',
            old_name='univesity',
            new_name='university',
        ),
    ]
