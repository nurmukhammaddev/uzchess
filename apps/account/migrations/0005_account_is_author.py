# Generated by Django 4.1.7 on 2023-03-23 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_account_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_author',
            field=models.BooleanField(default=False, verbose_name='Author'),
        ),
    ]
