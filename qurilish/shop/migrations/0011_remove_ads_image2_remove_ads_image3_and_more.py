# Generated by Django 4.1 on 2022-10-31 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0010_product_class_name_alter_product_number_company"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ads",
            name="image2",
        ),
        migrations.RemoveField(
            model_name="ads",
            name="image3",
        ),
        migrations.RemoveField(
            model_name="ads",
            name="image4",
        ),
        migrations.RemoveField(
            model_name="ads",
            name="name2",
        ),
        migrations.RemoveField(
            model_name="ads",
            name="name3",
        ),
        migrations.RemoveField(
            model_name="ads",
            name="name4",
        ),
    ]
