# Generated by Django 4.1.3 on 2023-07-28 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_customer_email_shippingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]