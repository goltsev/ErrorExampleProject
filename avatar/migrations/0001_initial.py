# Generated by Django 3.0.7 on 2020-06-26 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='test_folder/', verbose_name='avatar')),
            ],
            options={
                'verbose_name': 'Авы',
            },
        ),
    ]
