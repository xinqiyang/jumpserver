# Generated by Django 3.2.14 on 2023-02-21 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0110_auto_20230220_1051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asset',
            options={'ordering': ['name'], 'permissions': [('refresh_assethardwareinfo', 'Can refresh asset hardware info'), ('test_assetconnectivity', 'Can test asset connectivity'), ('push_assetaccount', 'Can push account to asset'), ('test_account', 'Can verify account'), ('match_asset', 'Can match asset'), ('change_assettonode', 'Can change asset nodes')], 'verbose_name': 'Asset'},
        ),
    ]
