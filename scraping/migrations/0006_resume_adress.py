# Generated by Django 3.2.6 on 2022-05-31 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0005_auto_20220530_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='adress',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
