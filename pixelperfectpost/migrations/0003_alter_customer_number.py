# Generated by Django 3.2 on 2021-04-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixelperfectpost', '0002_auto_20210421_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='number',
            field=models.IntegerField(),
        ),
    ]
