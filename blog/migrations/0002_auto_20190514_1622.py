# Generated by Django 2.0.13 on 2019-05-14 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='static/img'),
        ),
        migrations.AddField(
            model_name='art',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='static/img'),
        ),
        migrations.AddField(
            model_name='art',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='static/img'),
        ),
        migrations.AddField(
            model_name='project',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='static/img'),
        ),
        migrations.AddField(
            model_name='project',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='static/img'),
        ),
        migrations.AddField(
            model_name='project',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='static/img'),
        ),
    ]
