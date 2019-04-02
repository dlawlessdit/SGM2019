# Generated by Django 2.1.5 on 2019-03-27 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab7app', '0006_auto_20190327_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='image2',
            field=models.ImageField(blank=True, help_text='Upload the 1st image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image2_de',
            field=models.ImageField(blank=True, help_text='Upload the 1st image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image2_en',
            field=models.ImageField(blank=True, help_text='Upload the 1st image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image2_fr',
            field=models.ImageField(blank=True, help_text='Upload the 1st image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image3',
            field=models.ImageField(blank=True, help_text='Upload the 2nd image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image3_de',
            field=models.ImageField(blank=True, help_text='Upload the 2nd image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image3_en',
            field=models.ImageField(blank=True, help_text='Upload the 2nd image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image3_fr',
            field=models.ImageField(blank=True, help_text='Upload the 2nd image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image4',
            field=models.ImageField(blank=True, help_text='Upload the 3rd image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image4_de',
            field=models.ImageField(blank=True, help_text='Upload the 3rd image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image4_en',
            field=models.ImageField(blank=True, help_text='Upload the 3rd image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image4_fr',
            field=models.ImageField(blank=True, help_text='Upload the 3rd image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image5',
            field=models.ImageField(blank=True, help_text='Upload the 4th image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image5_de',
            field=models.ImageField(blank=True, help_text='Upload the 4th image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image5_en',
            field=models.ImageField(blank=True, help_text='Upload the 4th image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image5_fr',
            field=models.ImageField(blank=True, help_text='Upload the 4th image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image6',
            field=models.ImageField(blank=True, help_text='Upload the 5th image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image6_de',
            field=models.ImageField(blank=True, help_text='Upload the 5th image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image6_en',
            field=models.ImageField(blank=True, help_text='Upload the 5th image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image6_fr',
            field=models.ImageField(blank=True, help_text='Upload the 5th image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image7',
            field=models.ImageField(blank=True, help_text='Upload the 6th image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image7_de',
            field=models.ImageField(blank=True, help_text='Upload the 6th image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image7_en',
            field=models.ImageField(blank=True, help_text='Upload the 6th image for portfolio', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='image7_fr',
            field=models.ImageField(blank=True, help_text='Upload the 6th image for portfolio', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='page',
            name='image1',
            field=models.ImageField(blank=True, help_text='Upload the main image', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='page',
            name='image1_de',
            field=models.ImageField(blank=True, help_text='Upload the main image', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='page',
            name='image1_en',
            field=models.ImageField(blank=True, help_text='Upload the main image', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='page',
            name='image1_fr',
            field=models.ImageField(blank=True, help_text='Upload the main image', null=True, upload_to=''),
        ),
    ]