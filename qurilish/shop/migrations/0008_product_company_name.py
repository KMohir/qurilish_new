# Generated by Django 4.1 on 2022-10-05 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0007_remove_product_image3_remove_product_image4_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="company_name",
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
