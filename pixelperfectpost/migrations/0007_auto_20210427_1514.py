# Generated by Django 3.2 on 2021-04-27 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixelperfectpost', '0006_remove_customer_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='services/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='service',
            name='video',
            field=models.FileField(default=None, null=True, upload_to='sevices/%Y/%m/%d'),
        ),
    ]
