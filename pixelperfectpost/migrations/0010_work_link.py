# Generated by Django 3.2 on 2021-04-29 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixelperfectpost', '0009_remove_work_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='link',
            field=models.URLField(null=True),
        ),
    ]
