# Generated by Django 4.2.5 on 2023-09-19 13:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('swiftbill', '0007_rename_paystack_public_key_api_config_public_key_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserBalance',
            new_name='wallet',
        ),
    ]
