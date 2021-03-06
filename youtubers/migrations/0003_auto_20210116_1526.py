# Generated by Django 3.1.2 on 2021-01-16 09:56

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0002_youtuber_crew'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('nicon', 'nicon'), ('panasonic', 'panasonic'), ('fuji', 'fuji'), ('red', 'red'), ('sony', 'sony'), ('canon', 'canon')], max_length=50),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('solo', 'solo'), ('small', 'small-team(2-5)'), ('large', 'large-team(5+)')], max_length=50),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
