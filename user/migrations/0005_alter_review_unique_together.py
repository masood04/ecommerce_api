# Generated by Django 4.0.3 on 2022-05-18 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_discount_price'),
        ('user', '0004_review'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('product', 'user')},
        ),
    ]
