# Generated by Django 4.2.7 on 2023-12-29 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_transaction_bank_rupt'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transfer_account_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
