# Generated by Django 2.0.5 on 2018-07-31 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getrate', '0002_auto_20180731_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='currencyrate',
            name='sourceCode',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
