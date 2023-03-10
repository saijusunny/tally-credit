# Generated by Django 4.0.2 on 2023-01-11 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_payment_voucher_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='credit_note',
            fields=[
                ('screditid', models.AutoField(primary_key=True, serialize=False, verbose_name='cnid')),
                ('credit_no', models.IntegerField(default=1000)),
                ('customer', models.CharField(max_length=100, null=True)),
                ('creditdate', models.DateField(null=True)),
                ('ledger_acc', models.CharField(max_length=100, null=True)),
                ('subtotal', models.CharField(max_length=100, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('grandtotal', models.CharField(max_length=100, null=True)),
                ('comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.companies')),
            ],
        ),
        migrations.CreateModel(
            name='credit_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=100, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('price', models.CharField(max_length=100, null=True)),
                ('total', models.CharField(max_length=100, null=True)),
                ('scredit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.credit_note')),
            ],
        ),
    ]
