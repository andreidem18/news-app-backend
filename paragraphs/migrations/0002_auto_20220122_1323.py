# Generated by Django 2.2.24 on 2022-01-22 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paragraphs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='paragraph',
            field=models.TextField(),
        ),
    ]