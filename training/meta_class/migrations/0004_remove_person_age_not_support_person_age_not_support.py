# Generated by Django 4.2 on 2023-04-17 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta_class', '0003_alter_person_options_person_note_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='person',
            name='age_not_support',
        ),
        migrations.AddConstraint(
            model_name='person',
            constraint=models.CheckConstraint(check=models.Q(('age__gte', 6)), name='age_not_support'),
        ),
    ]
