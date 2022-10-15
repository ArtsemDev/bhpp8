# Generated by Django 4.1.1 on 2022-10-10 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_feedback_date_created_alter_order_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='картинка'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 10, 18, 19, 13, 782747, tzinfo=datetime.timezone.utc), verbose_name='дата публикации'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 10, 18, 19, 13, 781748, tzinfo=datetime.timezone.utc), verbose_name='дата'),
        ),
    ]