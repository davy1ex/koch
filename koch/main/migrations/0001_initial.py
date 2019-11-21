# Generated by Django 2.2.7 on 2019-11-20 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playground',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playground_type', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=128)),
                ('rating', models.IntegerField()),
                ('description', models.CharField(max_length=512)),
                ('latitude', models.FloatField(unique=True)),
                ('longitude', models.FloatField(unique=True)),
                ('photo', models.ImageField(upload_to='playground')),
            ],
        ),
    ]