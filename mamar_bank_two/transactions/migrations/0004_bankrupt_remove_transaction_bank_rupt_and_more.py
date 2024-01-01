# Generated by Django 4.2.7 on 2023-12-30 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_transaction_transfer_account_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bankrupt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_rupt', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='bank_rupt',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'Deposite'), (2, 'Withdrawal'), (3, 'Loan'), (4, 'Loan Paid'), (5, 'Transfer Money')], null=True),
        ),
    ]
