# Generated by Django 4.0.1 on 2022-01-08 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_posts_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
