# Generated by Django 3.2.4 on 2021-08-12 07:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0002_auto_20210617_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Order_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
