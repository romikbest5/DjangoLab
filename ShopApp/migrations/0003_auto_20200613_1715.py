# Generated by Django 3.0.5 on 2020-06-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0002_auto_20200613_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.ImageField(height_field=200, null=True, upload_to='images', width_field=200),
        ),
    ]