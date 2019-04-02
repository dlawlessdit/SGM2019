# Generated by Django 2.1.5 on 2019-03-29 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab7app', '0013_auto_20190328_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='book',
        ),
        migrations.AlterField(
            model_name='page',
            name='mainimage',
            field=models.ImageField(blank=True, help_text='Upload the main image', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='page',
            name='mainimage_de',
            field=models.ImageField(blank=True, help_text='Upload the main image', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='page',
            name='mainimage_en',
            field=models.ImageField(blank=True, help_text='Upload the main image', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='page',
            name='mainimage_fr',
            field=models.ImageField(blank=True, help_text='Upload the main image', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='pageimages',
            name='imfile',
            field=models.ImageField(blank=True, help_text='Upload the file', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='pageimages',
            name='imfile_de',
            field=models.ImageField(blank=True, help_text='Upload the file', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='pageimages',
            name='imfile_en',
            field=models.ImageField(blank=True, help_text='Upload the file', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='pageimages',
            name='imfile_fr',
            field=models.ImageField(blank=True, help_text='Upload the file', null=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='BookInstance',
        ),
    ]