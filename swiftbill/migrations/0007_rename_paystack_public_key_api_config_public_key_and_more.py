# Generated by Django 4.2.5 on 2023-09-19 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swiftbill', '0006_userbalance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='api_config',
            old_name='PAYSTACK_PUBLIC_KEY',
            new_name='PUBLIC_KEY',
        ),
        migrations.RenameField(
            model_name='api_config',
            old_name='PAYSTACK_SECRET_KEY',
            new_name='SECRET_KEY',
        ),
        migrations.RenameField(
            model_name='api_config',
            old_name='TEST_PAYSTACK_PUBLIC_KEY',
            new_name='TEST_PUBLIC_KEY',
        ),
        migrations.RenameField(
            model_name='api_config',
            old_name='TEST_PAYSTACK_SECRET_KEY',
            new_name='TEST_SECRET_KEY',
        ),
    ]
