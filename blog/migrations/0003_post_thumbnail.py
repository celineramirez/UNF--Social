# Generated by Django 4.1.2 on 2022-10-23 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_created_date_post_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.URLField(blank=True),
        ),
    ]
