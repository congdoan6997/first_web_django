# Generated by Django 3.0.1 on 2019-12-22 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='This is a text'),
            preserve_default=False,
        ),
    ]
