# Generated by Django 3.1 on 2020-08-30 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0006_auto_20200831_0026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gradedassignment',
            old_name='question',
            new_name='asnt',
        ),
    ]
