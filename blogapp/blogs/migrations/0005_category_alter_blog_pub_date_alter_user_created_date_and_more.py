# Generated by Django 4.2 on 2023-04-24 05:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_category_alter_blog_options_user_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(
                2023, 4, 24, 5, 31, 50, 36882, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(
                2023, 4, 24, 5, 31, 50, 36882, tzinfo=datetime.timezone.utc)),
        ),
    ]
