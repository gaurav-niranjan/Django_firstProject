# Generated by Django 3.2.5 on 2021-09-11 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_demo_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='titile',
            new_name='title',
        ),
    ]
