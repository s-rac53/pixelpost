# Generated by Django 3.2 on 2021-04-27 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixelperfectpost', '0004_alter_customer_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='area',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='customer',
            name='extension',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
