# Generated by Django 4.2.5 on 2023-10-04 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swiftbill', '0010_alter_wallet_balance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='api_config',
            old_name='PUBLIC_KEY',
            new_name='GIFTBILL_PUBLIC_KEY',
        ),
        migrations.RenameField(
            model_name='api_config',
            old_name='SECRET_KEY',
            new_name='GIFTBILL_SECRET_KEY',
        ),
        migrations.RenameField(
            model_name='api_config',
            old_name='TEST_PUBLIC_KEY',
            new_name='PAYSTACK_PUBLIC_KEY',
        ),
        migrations.RenameField(
            model_name='api_config',
            old_name='TEST_SECRET_KEY',
            new_name='PAYSTACK_SECRET_KEY',
        ),
    ]