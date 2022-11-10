# Generated by Django 4.1 on 2022-10-17 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0008_product_company_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="ads",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name1", models.CharField(db_index=True, max_length=250)),
                (
                    "image1",
                    models.ImageField(
                        blank=True, null=True, upload_to="products/%y/%m/%d"
                    ),
                ),
                ("name2", models.CharField(db_index=True, max_length=250)),
                (
                    "image2",
                    models.ImageField(
                        blank=True, null=True, upload_to="products/%y/%m/%d"
                    ),
                ),
                ("name3", models.CharField(db_index=True, max_length=250)),
                (
                    "image3",
                    models.ImageField(
                        blank=True, null=True, upload_to="products/%y/%m/%d"
                    ),
                ),
                ("name4", models.CharField(db_index=True, max_length=250)),
                (
                    "image4",
                    models.ImageField(
                        blank=True, null=True, upload_to="products/%y/%m/%d"
                    ),
                ),
            ],
        ),
    ]