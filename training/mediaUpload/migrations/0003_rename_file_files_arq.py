# Generated by Django 4.2 on 2023-04-07 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediaUpload', '0002_alter_files_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='files',
            old_name='file',
            new_name='arq',
        ),
    ]
