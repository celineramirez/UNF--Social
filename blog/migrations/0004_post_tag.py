# Generated by Django 4.1.3 on 2022-12-01 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(blank=True, choices=[('tag1', 'tag1'), ('tag2', 'tag2'), ('tag3', 'tag3'), ('tag4', 'tag4'), ('tag5', 'tag5')], max_length=15, null=True),
        ),
    ]
