# Generated by Django 4.0.4 on 2022-05-31 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='name',
            new_name='title',
        ),
    ]
