# Generated by Django 2.1.5 on 2019-02-19 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='imprint',
        ),
    ]
