# Generated by Django 2.2.5 on 2022-05-04 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20220505_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
    ]
