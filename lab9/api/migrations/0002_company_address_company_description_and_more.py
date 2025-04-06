# Generated by Django 5.1.7 on 2025-03-30 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(default='suu'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='description',
            field=models.TextField(default='No description yet'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='salary',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
