# Generated by Django 2.1.5 on 2019-03-27 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab7app', '0002_auto_20190326_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('title', models.CharField(help_text='Enter the title of the page', max_length=20)),
                ('desc', models.CharField(help_text='Enter a description of the page (will appear on the page)', max_length=100)),
            ],
        ),
    ]
