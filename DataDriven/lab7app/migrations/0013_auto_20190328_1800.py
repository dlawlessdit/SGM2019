# Generated by Django 2.1.5 on 2019-03-28 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab7app', '0012_auto_20190328_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pageimages',
            old_name='pagename',
            new_name='page',
        ),
    ]
