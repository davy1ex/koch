# Generated by Django 2.2.7 on 2019-12-28 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playgrounds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playground',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='playground', verbose_name='Photo'),
        ),
    ]