# Generated by Django 5.0.2 on 2024-02-10 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_profile_image_alter_profile_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='untersuchengs price:'),
        ),
    ]
