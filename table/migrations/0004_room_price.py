# Generated by Django 3.2.5 on 2021-08-04 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0003_order_order_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]