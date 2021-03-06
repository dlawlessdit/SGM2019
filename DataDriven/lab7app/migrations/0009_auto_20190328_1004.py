# Generated by Django 2.1.5 on 2019-03-28 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab7app', '0008_auto_20190327_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imname', models.CharField(max_length=20, unique=True)),
                ('imalt', models.CharField(help_text='Enter the alt text to display', max_length=50, unique=True)),
                ('imalt_en', models.CharField(help_text='Enter the alt text to display', max_length=50, null=True, unique=True)),
                ('imalt_de', models.CharField(help_text='Enter the alt text to display', max_length=50, null=True, unique=True)),
                ('imalt_fr', models.CharField(help_text='Enter the alt text to display', max_length=50, null=True, unique=True)),
                ('imfile', models.ImageField(blank=True, help_text='Upload the file', null=True, upload_to='.')),
                ('imfile_en', models.ImageField(blank=True, help_text='Upload the file', null=True, upload_to='.')),
                ('imfile_de', models.ImageField(blank=True, help_text='Upload the file', null=True, upload_to='.')),
                ('imfile_fr', models.ImageField(blank=True, help_text='Upload the file', null=True, upload_to='.')),
            ],
        ),
        migrations.RemoveField(
            model_name='page',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='page',
            name='image1_de',
        ),
        migrations.RemoveField(
            model_name='page',
            name='image1_en',
        ),
        migrations.RemoveField(
            model_name='page',
            name='image1_fr',
        ),
        migrations.RemoveField(
            model_name='page',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='page',
            name='image2_de',
        ),
        migrations.RemoveField(
            model_name='page',
            name='image2_en',
        ),
        migrations.RemoveField(
            model_name='page',
            name='image2_fr',
        ),
        migrations.RemoveField(
            model_name='page',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='page',
            name='image3_de',
        ),
        migrations.RemoveField(
            model_name='page',
            name='image3_en',
        ),
        migrations.RemoveField(
            model_name='page',
            name='image3_fr',
        ),
        migrations.RemoveField(
            model_name='page',
            name='image4',
        ),
        migrations.AddField(
            model_name='page',
            name='mainimage',
            field=models.ImageField(blank=True, help_text='Upload the main image', null=True, upload_to='.'),
        ),
        migrations.AddField(
            model_name='page',
            name='mainimage_de',
            field=models.ImageField(blank=True, help_text='Upload the main image', null=True, upload_to='.'),
        ),
        migrations.AddField(
            model_name='page',
            name='mainimage_en',
            field=models.ImageField(blank=True, help_text='Upload the main image', null=True, upload_to='.'),
        ),
        migrations.AddField(
            model_name='page',
            name='mainimage_fr',
            field=models.ImageField(blank=True, help_text='Upload the main image', null=True, upload_to='.'),
        ),
        migrations.AddField(
            model_name='pageimages',
            name='page',
            field=models.ManyToManyField(help_text='Select a page that this image belongs to', to='lab7app.Page'),
        ),
    ]
