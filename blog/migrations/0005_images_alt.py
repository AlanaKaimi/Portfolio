# Generated by Django 2.0.13 on 2019-06-28 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190514_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='alt',
            field=models.TextField(default=""),
        ),
    ]
