# Generated by Django 5.0.7 on 2024-07-14 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_vendor_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pdf_description',
            field=models.FileField(blank=True, null=True, upload_to='product_pdfs/'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]