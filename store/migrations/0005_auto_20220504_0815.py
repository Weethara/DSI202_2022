# Generated by Django 2.2.5 on 2022-05-04 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
